# The locked rubric

The criteria your supervisor and opponent actually fill in, quoted from the form itself.

Every defended thesis at Charles University is published in the university repository together
with both referee reports, so this form is a public document. The text in the boxed sections below
is copied word for word. Do not paraphrase it anywhere in this repository.

**Last verified:** 2026-08-03, against 230 filed reports covering 115 IES master's theses defended
between 2023 and 2026. Re-verify annually; see `docs/for_supervisors.md`.

---

## The form

```
Report on Master Thesis
Institute of Economic Studies, Faculty of Social Sciences, Charles University

SUMMARY OF POINTS AWARDED:

CATEGORY                                POINTS
Contribution              (max. 30 points)
Methods                   (max. 30 points)
Literature                (max. 20 points)
Manuscript Form           (max. 20 points)
TOTAL POINTS              (max. 100 points)
GRADE                     (A - B - C - D - E - F)

Overall grading:
  91 - 100   A
  81 -  90   B
  71 -  80   C
  61 -  70   D
  51 -  60   E
   0 -  50   F
```

## The four categories, verbatim

> **CONTRIBUTION:** The author presents original ideas on the topic demonstrating critical thinking
> and ability to draw conclusions based on the knowledge of relevant theory and empirics. There is
> a distinct value added of the thesis.

> **METHODS:** The tools used are relevant to the research question being investigated, and
> adequate to the author's level of studies. The thesis topic is comprehensively analyzed.

> **LITERATURE REVIEW:** The thesis demonstrates author's full understanding and command of recent
> literature. The author quotes relevant literature in a proper way.

> **MANUSCRIPT FORM:** The thesis is well structured. The student uses appropriate language and
> style, including academic format for graphs and tables. The text effectively refers to graphs and
> tables and disposes with a complete bibliography.

The report also requires a short summary of the thesis, a written assessment of each of the four
categories, an overall evaluation, suggested questions for the defence, a statement on text
similarity, and an explicit recommendation for or against defence. The stated minimum length is
300 words.

---

## Why this tool never gives you a number

The tool works from the four categories above and never reports points, a total, or a grade. Four
reasons, each measured on the 230 reports.

**The form is filled loosely.** One report in the sample awards 30 points in a box whose maximum is
20, and totals it at 99 anyway. Reports that would be arithmetically identical get different
grades.

**The form is not uniform.** Of the 230 reports, 196 use the plain four-category version, 12 add
Strong/Average/Weak anchors to the same categories, and 3 use a five-category variant with
Theoretical background as a separate heading at 20 points. Nineteen could not be parsed.

**Referees disagree with each other, hard.** Two reports in the sample penalise a thesis for
comparing forecast errors without a statistical test. A third thesis does the same thing and
receives full marks for Methods. One award-winning thesis states that its models were tuned to
maximise performance on the sample it then evaluates them on, and its opponent awarded Methods
30/30 and 100/100 overall.

**Supervisors and opponents are not the same reader.** Mean total across the sample is 89.5 from
supervisors and 82.6 from opponents, a gap of 6.9 points. The opponent is the binding constraint,
so this tool is calibrated to the opponent and says so in its output. It is not predicting what
your supervisor will write.

A predicted number built on that would be noise, and a student who received one would optimise
against it. So the tool gives verdicts and repairs instead: for each category, whether the current
draft is *defensible*, *at risk*, or *not defensible as written*, and what specific change would
lift it.

---

## What the distribution actually looks like

From the 176 reports in the sample that carry a parsable points table, for context only. These are
not targets.

| | mean | sd | min | p10 | median |
|---|---|---|---|---|---|
| Total (max 100) | 86.1 | 12.2 | 45 | 70 | 91 |
| Contribution (30) | 25.3 | 4.6 | 6 | 20 | |
| Methods (30) | 26.1 | 4.1 | 10 | 20 | |
| Literature (20) | 17.9 | 2.7 | 5 | 15 | |
| Manuscript Form (20) | 17.0 | 3.2 | 5 | 12 | |

Grades across 181 reports: A 91, B 37, C 31, D 12, E 8, F 2.

Two things follow. Half of all reports recommend an A, so a good grade is not evidence of a good
thesis and the form cannot be the target. And **Contribution has the widest spread and the lowest
floor**, which makes it the category that separates theses and the one hardest to repair late. The
tool weights its attention accordingly.

---

## Where referee attention actually goes

Share of the 230 reports whose text raises each issue:

| issue | share |
|---|---|
| formatting, tables, figures | 28.7% |
| typos, language, proofreading | 25.2% |
| robustness, sensitivity | 21.3% |
| literature thin or outdated | 18.3% |
| endogeneity | 17.4% |
| causality | 10.9% |
| identification strategy | 10.0% |
| instruments, IV | 9.1% |
| "descriptive, not causal" | 9.1% |
| publication bias | 7.8% |
| external validity | 5.7% |
| clustering, standard errors | 3.9% |
| replication package or code | 0.9% |

The two problems referees write about most are formatting and typos. Both are mechanical, and
clearing them before a human reads the draft is the point of `basic/prompt_form_sweep.md`. What is
left is the reader's attention on the design.

One caveat on publication bias: the 7.8% is composition, not a general concern. Meta-analyses are
about 11% of the cohort, and 16 of 19 meta-analysis reports discuss publication bias against 1 of
181 others. It belongs in the meta-analysis route, not the core.

---

## Sources

- The form and both report types, from the Charles University Digital Repository,
  `dspace.cuni.cz`. Every defended thesis carries `Posudek vedoucího` and `Posudek oponenta` as
  public attachments.
- Course requirements: the JEM001 and JEM002 syllabi in the Student Information System,
  `is.cuni.cz`.
- The proposal template and the thesis templates, from the JEM213 file area in the Student
  Information System.

The IES report form and the course materials remain the property of the Institute of Economic
Studies and are quoted here for use by that institute's own students.
