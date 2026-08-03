#!/usr/bin/env python3
"""Mechanical completeness check over a folder of Seminar Cards.

Checks form, never content. A card passes if the student filled it in; nothing here
judges whether what they wrote is any good. That is what the seminar is for.

Usage:
    python card_check.py <folder> [--milestone JEM001-2] [--csv out.csv]

Reads .txt, .md and .card files. Prints a per-student pass/fail table and a digest of
the header fields, which is what an instructor scans before a session.
"""

import argparse
import csv
import os
import re
import sys
from collections import Counter

MILESTONES = ["JEM001-1", "JEM001-2", "JEM001-3", "JEM002-1", "JEM002-2", "JEM002-3"]
FAMILIES = ["causal-micro", "time-series-macro", "financial-econometrics",
            "forecasting-ML", "meta-analysis", "structural-or-descriptive"]
DATA_STATUS = ["none", "requested", "in hand, not cleaned", "analysis-ready"]

# A past-tense attempt, not a plan. "I will run" / "I plan to" / "I am going to" fail.
PLAN_RX = re.compile(r"\b(i (will|plan to|intend to|am going to|would)|going to|next step)\b", re.I)
PAST_RX = re.compile(r"\b(ran|re-?ran|estimated|tested|dropped|added|checked|compared|computed|"
                     r"restricted|excluded|replicated|plotted|split|winsoriz\w+|bootstrapp\w+|"
                     r"did|used|applied|implemented|verified|examined|repeated)\b", re.I)
PLACEHOLDER_RX = re.compile(r"^[\s.\-_]*$")

SECTION_RX = {
    "claim": re.compile(r"---\s*1\..*?---(.*?)(?=---\s*2\.|\Z)", re.S | re.I),
    "threat": re.compile(r"---\s*2\..*?---(.*?)(?=---\s*3\.|\Z)", re.S | re.I),
    "adjudicate": re.compile(r"---\s*3\..*?---(.*?)(?=---\s*4\.|\Z)", re.S | re.I),
    "carried": re.compile(r"---\s*4\..*?---(.*?)(?====\s*END|\Z)", re.S | re.I),
}


def field(text, name):
    # Labels may sit mid-line, so do not anchor to line start.
    m = re.search(rf"\b{name}\s*:\s*(.*)$", text, re.I | re.M)
    if not m:
        return ""
    v = m.group(1).strip()
    # Two fields can share a line ("STUDENT: X   SUPERVISOR: Y"); stop at the next label.
    v = re.split(r"\s{2,}[A-Z][A-Z /-]{2,}\s*:", v)[0].strip()
    # An unedited template slot is not a value.
    if PLACEHOLDER_RX.match(v) or (v.startswith("[") and v.endswith("]")):
        return ""
    return v


def section(text, key):
    m = SECTION_RX[key].search(text)
    return m.group(1).strip() if m else ""


def substantive(block):
    """Strip template scaffolding and see whether anything was actually written."""
    out = []
    for line in block.splitlines():
        s = line.strip()
        if not s or set(s) <= set(".-_= "):
            continue
        s = re.sub(r"\.{3,}", " ", s)
        # drop pure label lines like "Attempt:" with nothing after
        if re.match(r"^[A-Za-z][A-Za-z /()'-]{0,40}:\s*$", s):
            continue
        s = re.sub(r"^[A-Za-z][A-Za-z /()'-]{0,40}:\s*", "", s)
        if re.fullmatch(r"\[.*\]", s):
            continue
        if len(s) >= 8:
            out.append(s)
    return " ".join(out)


def check(text):
    """Return (list of failures, dict of header fields, dict of flags)."""
    fails, flags = [], {}

    hdr = {k: field(text, k.replace("_", " ")) for k in
           ("STUDENT", "SUPERVISOR", "MILESTONE", "DATE", "DATA_STATUS")}
    hdr["DESIGN_FAMILY"] = field(text, "DESIGN FAMILY")
    hdr["AI_PRE_REVIEW"] = field(text, "AI PRE-REVIEW")
    hdr["DATA_STATUS"] = field(text, "DATA STATUS")

    for k in ("STUDENT", "SUPERVISOR", "MILESTONE", "DATE"):
        if not hdr[k]:
            fails.append(f"header {k} empty")

    if hdr["MILESTONE"] and not any(m in hdr["MILESTONE"] for m in MILESTONES):
        fails.append("MILESTONE not one of the six")
    if not hdr["DESIGN_FAMILY"]:
        fails.append("DESIGN FAMILY empty")
    elif not any(f.lower() in hdr["DESIGN_FAMILY"].lower() for f in FAMILIES):
        fails.append("DESIGN FAMILY not one of the six")
    if not hdr["DATA_STATUS"]:
        fails.append("DATA STATUS empty")
    if not hdr["AI_PRE_REVIEW"]:
        fails.append("AI PRE-REVIEW empty (write 'not run' if you did not)")

    # 1 - the claim
    if len(substantive(section(text, "claim"))) < 60:
        fails.append("section 1 (claim) not filled in")

    # 2 - the threat, and the attempt in past tense
    threat = section(text, "threat")
    body = substantive(threat)
    if len(body) < 60:
        fails.append("section 2 (threat) not filled in")
    else:
        verdict = ""
        mv = re.search(r"Verdict\s*:\s*(.+)", threat, re.I)
        if mv:
            verdict = mv.group(1).strip()
        excused = bool(re.search(r"could not check yet because\s*\S", verdict, re.I))
        attempt = ""
        ma = re.search(r"Attempt\s*:\s*(.+?)(?=\n\s*(Result|Verdict)\s*:|\Z)", threat, re.S | re.I)
        if ma:
            attempt = substantive(ma.group(1))
        if not verdict or re.fullmatch(r"\[.*\]", verdict):
            fails.append("section 2 Verdict missing")
        elif not excused:
            if len(attempt) < 15:
                fails.append("section 2 Attempt empty and no reason given")
            elif PLAN_RX.search(attempt) and not PAST_RX.search(attempt):
                fails.append("section 2 Attempt is a plan, not something you did")
                flags["plan_not_attempt"] = True
        if excused:
            flags["no_attempt_yet"] = True

    # 3 - at most three, each binary
    adj = section(text, "adjudicate")
    qs = [q.strip() for q in re.findall(r"^\s*Q\d\.\s*(.+)$", adj, re.M) if substantive(q)]
    if not qs:
        fails.append("section 3 has no question")
    if len(qs) > 3:
        fails.append(f"section 3 has {len(qs)} questions, maximum is 3")
    for i, q in enumerate(qs, 1):
        if not (re.search(r"\[A\]", q) and re.search(r"\[B\]", q)):
            fails.append(f"section 3 Q{i} is not an A-or-B choice")
    flags["n_questions"] = len(qs)

    # 4 - carried forward
    carried = substantive(section(text, "carried"))
    first = hdr["MILESTONE"].strip().startswith("JEM001-1")
    if not carried and not first:
        fails.append("section 4 empty (write 'none' only at your first milestone)")
    if carried:
        statuses = re.findall(r"\b(closed|partly addressed|unaddressed)\b", carried, re.I)
        if not statuses:
            fails.append("section 4 items carry no status")
        flags["unaddressed"] = sum(1 for s in statuses if s.lower() == "unaddressed")

    return fails, hdr, flags


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--milestone", help="only cards for this milestone")
    ap.add_argument("--csv", help="write results here")
    a = ap.parse_args()

    if not os.path.isdir(a.folder):
        sys.exit(f"not a folder: {a.folder}")

    rows = []
    for fn in sorted(os.listdir(a.folder)):
        if not fn.lower().endswith((".txt", ".md", ".card")):
            continue
        p = os.path.join(a.folder, fn)
        try:
            text = open(p, encoding="utf-8", errors="replace").read()
        except OSError as e:
            print(f"  cannot read {fn}: {e}")
            continue
        if "IES THESIS SEMINAR CARD" not in text.upper():
            rows.append({"file": fn, "student": "", "fails": ["not a Seminar Card"],
                         "hdr": {}, "flags": {}})
            continue
        fails, hdr, flags = check(text)
        if a.milestone and a.milestone not in hdr.get("MILESTONE", ""):
            continue
        rows.append({"file": fn, "student": hdr.get("STUDENT", ""), "fails": fails,
                     "hdr": hdr, "flags": flags})

    if not rows:
        sys.exit("no cards found")

    passed = [r for r in rows if not r["fails"]]
    failed = [r for r in rows if r["fails"]]

    print(f"\n{len(rows)} cards -- {len(passed)} pass, {len(failed)} incomplete\n")

    if failed:
        print("INCOMPLETE")
        for r in failed:
            who = r["student"] or r["file"]
            print(f"  {who}")
            for f in r["fails"]:
                print(f"      - {f}")
        print()

    fam = Counter(r["hdr"].get("DESIGN_FAMILY", "?") for r in rows if r["hdr"])
    ds = Counter(r["hdr"].get("DATA_STATUS", "?") for r in rows if r["hdr"])
    print("DESIGN FAMILY: " + " | ".join(f"{k} {v}" for k, v in fam.most_common()))
    print("DATA STATUS:   " + " | ".join(f"{k} {v}" for k, v in ds.most_common()))

    no_attempt = [r for r in rows if r["flags"].get("no_attempt_yet")]
    stuck = [r for r in rows if r["flags"].get("unaddressed", 0) > 0]
    early = [r for r in rows if r["hdr"].get("DATA_STATUS", "").lower().startswith(("none", "requested"))
             and not r["hdr"].get("MILESTONE", "").endswith("1-1")]
    print()
    if no_attempt:
        print(f"  {len(no_attempt)} could not attempt the threat yet")
    if early:
        print(f"  {len(early)} still without data past the first milestone  <- schedule risk")
    if stuck:
        print(f"  {len(stuck)} carrying an unaddressed item forward")

    if a.csv:
        with open(a.csv, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["file", "student", "supervisor", "milestone", "design_family",
                        "data_status", "ai_pre_review", "pass", "failures"])
            for r in rows:
                h = r["hdr"]
                w.writerow([r["file"], r["student"], h.get("SUPERVISOR", ""),
                            h.get("MILESTONE", ""), h.get("DESIGN_FAMILY", ""),
                            h.get("DATA_STATUS", ""), h.get("AI_PRE_REVIEW", ""),
                            "yes" if not r["fails"] else "no", "; ".join(r["fails"])])
        print(f"\nwritten: {a.csv}")


if __name__ == "__main__":
    main()
