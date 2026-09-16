#!/usr/bin/env python3
"""count.py -- rough length check for an IES master's thesis draft.

This script counts characters, words, and (where the introduction and
conclusion can be found with confidence) the length of the thesis body.
It does not grade, judge, or decide whether a thesis meets any
requirement -- it measures, and prints the measured number next to the
faculty's stated threshold. The student draws the conclusion.

Usage:
    python count.py thesis.txt
    python count.py thesis.docx
    python count.py thesis.pdf
    py count.py thesis.docx        (Windows, if 'python' is not on PATH)

Supported input: .txt, .md, .tex, .docx, .pdf
Standard library only for .txt/.md/.tex.
.docx needs python-docx (pip install python-docx).
.pdf needs pypdf (pip install pypdf).
"""

import argparse
import re
import sys
from pathlib import Path

CHARS_PER_PAGE = 1800
FULL_MIN_PAGES, FULL_MIN_CHARS = 50, 90_000
FULL_MIN_PAGES_CS, FULL_MIN_CHARS_CS = 60, 108_000  # Czech or Slovak
PART_MIN_PAGES, PART_MIN_CHARS = 15, 27_000
SUPPORTED_EXTS = {".txt", ".md", ".tex", ".docx", ".pdf"}

# Heading regexes match a WHOLE line (or, for .tex, an extracted section title)
# so a word appearing mid-sentence in body text is never mistaken for a heading.
RE_INTRO = re.compile(r"^(chapter\s+)?(\d+(\.\d+)*\.?\s*)?introduction\s*$", re.I)
RE_CONCLUSION = re.compile(r"^(chapter\s+)?(\d+(\.\d+)*\.?\s*)?(conclusion|conclusions|concluding remarks)\s*$", re.I)
RE_REFERENCES = re.compile(r"^(references|bibliography|works cited)\s*$", re.I)
RE_APPENDIX = re.compile(r"^appendi(x|ces)\b", re.I)
RE_TEX_SECTION = re.compile(r"\\(?:chapter|section)\*?\{([^}]*)\}", re.I)
RE_TEX_BIB = re.compile(r"\\begin\{thebibliography\}|\\bibliography\{|\\printbibliography|\\addbibresource", re.I)
RE_TEX_APPENDIX = re.compile(r"^\\appendix\b", re.I)

def read_docx(path):
    try:
        import docx
    except ImportError:
        print("Reading .docx needs python-docx -- install with: pip install python-docx", file=sys.stderr)
        sys.exit(1)
    document = docx.Document(str(path))
    parts = [p.text for p in document.paragraphs]
    for table in document.tables:
        for row in table.rows:
            parts.extend(cell.text for cell in row.cells)
    return "\n".join(parts)

def read_pdf(path):
    try:
        import pypdf
    except ImportError:
        print("Reading .pdf needs pypdf -- install with: pip install pypdf", file=sys.stderr)
        sys.exit(1)
    reader = pypdf.PdfReader(str(path))
    pages = []
    for page in reader.pages:
        try:
            pages.append(page.extract_text() or "")
        except Exception:
            pages.append("")  # one damaged page should not sink the whole count
    return "\n".join(pages)

def extract_text(path, ext):
    if ext in (".txt", ".md", ".tex"):
        return path.read_text(encoding="utf-8", errors="replace")
    if ext == ".docx":
        return read_docx(path)
    return read_pdf(path)

def tex_heading_candidates(lines):
    """Map each .tex line to a heading title, or '' if it is not a heading command."""
    candidates = []
    for line in lines:
        stripped = line.strip()
        m = RE_TEX_SECTION.search(stripped)
        if m:
            candidates.append(m.group(1).strip())
        elif RE_TEX_BIB.search(stripped):
            candidates.append("References")
        elif RE_TEX_APPENDIX.match(stripped):
            candidates.append("Appendix")
        else:
            candidates.append("")
    return candidates

def find_main_body(text, is_tex):
    """Return the introduction-to-conclusion slice, or None if not confident.

    A thesis names its chapters twice: once in the table of contents and once where the
    chapter actually starts. Taking the first match gives the contents entry and a body a
    couple of pages long, so every candidate pair is tried and the longest plausible one
    wins. If nothing plausible survives, we say so rather than report a wrong number.
    """
    lines = text.splitlines()
    candidates = tex_heading_candidates(lines) if is_tex else [l.strip() for l in lines]
    total = len(text)

    intros = [i for i, c in enumerate(candidates) if c and RE_INTRO.match(c)]
    conclusions = [i for i, c in enumerate(candidates) if c and RE_CONCLUSION.match(c)]
    if not intros or not conclusions:
        return None

    best = None
    for intro_idx in intros:
        later = [j for j in conclusions if j > intro_idx]
        if not later:
            continue
        conclusion_idx = later[-1]  # the chapter, not a mention in the contents
        end_idx = len(lines)
        for i in range(conclusion_idx + 1, len(candidates)):
            if candidates[i] and (RE_REFERENCES.match(candidates[i]) or RE_APPENDIX.match(candidates[i])):
                end_idx = i
                break
        body = chr(10).join(lines[intro_idx:end_idx])
        if best is None or len(body) > len(best):
            best = body

    # A real main body is most of the document. Anything tiny means we locked on to the
    # table of contents or a stray mention, and a confident wrong number is worse than none.
    if best is None or total == 0 or len(best) < 0.25 * total:
        return None
    return best

def detect_references(text):
    lines = text.splitlines()
    heading_idx = next((i for i, l in enumerate(lines) if RE_REFERENCES.match(l.strip())), None)
    if heading_idx is not None:
        year_re = re.compile(r"(19|20)\d{2}")
        following = lines[heading_idx + 1 : heading_idx + 400]
        hits = sum(1 for l in following if year_re.search(l))
        return "yes" if hits >= 3 else "not sure"
    if RE_TEX_BIB.search(text):
        return "yes"
    if re.search(r"\breferences\b|\bbibliography\b", text, re.I):
        return "not sure"
    return "no"

def detect_summary_stats(text):
    lower = text.lower()
    keywords = ("mean", "std. dev", "std dev", "standard deviation", "minimum", "maximum", "observations")
    hits = sum(1 for kw in keywords if kw in lower)
    if re.search(r"descriptive statistics|summary statistics", lower):
        hits += 1  # the phrase is one signal, not proof: it also appears in "we report no ..."
    if hits >= 3:
        return "yes"
    return "not sure" if hits >= 1 else "no"

def counts(text):
    chars = len(text)
    return chars, chars / CHARS_PER_PAGE, len(text.split())

def main():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    parser = argparse.ArgumentParser(description="Measure the length of a thesis draft. Counts only -- no grading.")
    parser.add_argument("path", help="path to a .txt, .md, .tex, .docx or .pdf file")
    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        sys.exit(1)
    if not path.is_file():
        print(f"Not a file: {path}", file=sys.stderr)
        sys.exit(1)

    ext = path.suffix.lower()
    if ext not in SUPPORTED_EXTS:
        print(f"Unsupported file type '{ext or path.name}'. Use .txt, .md, .tex, .docx or .pdf.", file=sys.stderr)
        sys.exit(1)

    try:
        text = extract_text(path, ext)
    except Exception as e:
        print(f"Could not read file ({type(e).__name__}: {e})", file=sys.stderr)
        sys.exit(1)

    if not text.strip():
        print("File is empty, or no text could be extracted from it.", file=sys.stderr)
        sys.exit(1)

    print(f"File: {path.name}")
    if ext == ".pdf":
        print("Note: PDF text extraction is approximate -- whitespace, hyphenation, ligatures and")
        print("running headers can all shift the count. Treat these numbers as estimates.")
    if ext == ".tex":
        print("Note: this counts LaTeX SOURCE, not the rendered thesis a reader sees -- commands,")
        print("comments and \\input files are not filtered out. Counting the compiled PDF is more reliable.")

    total_chars, total_pages, total_words = counts(text)
    print(f"\nWhole document: {total_chars:,} characters incl. spaces, {total_pages:.1f} standard pages, {total_words:,} words")

    body = find_main_body(text, is_tex=(ext == ".tex"))
    if body is None:
        print("\nCould not identify the main body (introduction to conclusion) reliably;")
        print("showing whole-document counts only.")
    else:
        body_chars, body_pages, body_words = counts(body)
        print(f"\nMain body (introduction to conclusion): {body_chars:,} characters incl. spaces, "
              f"{body_pages:.1f} standard pages, {body_words:,} words")
        for label, min_pages, min_chars in (
            ("Full thesis in English", FULL_MIN_PAGES, FULL_MIN_CHARS),
            ("Full thesis in Czech or Slovak", FULL_MIN_PAGES_CS, FULL_MIN_CHARS_CS),
            ("First-part milestone", PART_MIN_PAGES, PART_MIN_CHARS),
        ):
            print(f"  {label} stated minimum is {min_pages} standard pages / {min_chars:,} characters; "
                  f"this measures {body_pages:.1f} pages / {body_chars:,} characters.")

    print(f"\nReferences list appears present: {detect_references(text)}")
    print(f"Summary/descriptive statistics table appears present: {detect_summary_stats(text)}")

if __name__ == "__main__":
    main()
