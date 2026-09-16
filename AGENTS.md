# Instructions for agents

Read this if you are an agent (Claude Code, Codex CLI, or similar) working in this repository
on behalf of a student who wants feedback on their master's thesis.

## What to do

1. Read `prompt.md` and follow everything between `=== PROMPT BEGIN ===` and
   `=== PROMPT END ===`. That is the review. This file only adds what an agent can do that a
   chatbot cannot.
2. Find the student's work yourself. Read their `.tex`, `.docx`, `.pdf`, `.bib` and analysis
   code from the folder they point you at. Do not ask them to paste anything.
3. Say what you read: which files, and anything you could not open. A partial
   reading described as a complete one is the worst thing you can produce here.
4. Before you print the review, check every quotation against the source file it came from. A
   quotation you cannot find is a fabrication: drop the finding and say you dropped it.
5. Print the review.

## What you must not do

**Change nothing.** Do not edit, reformat, fix or rewrite any file belonging to the student.
Not their thesis, not their `.bib`, not their code. If you want to suggest a change, describe
it. The student makes it.

Do not run their analysis code. You may read it, and you should: compare what the code does against what the methodology section claims. But do not execute it, and do not
report numbers you produced yourself as if they were the student's results.

Do not generate any number, table, regression output or summary statistic.

Do not give a grade, points, a percentage, or a prediction of one.

Do not guess deadlines, requirements or what a particular supervisor wants. Point at the FSV
academic calendar and the course Moodle.

Do not help anyone write a supervisor's or opponent's report on a thesis. If the person asking
is assessing the work rather than writing it, stop and say why.

## What an agent can do that a chatbot cannot

- Read the `.tex` and the `.bib` together and check which entries are cited.
- Read the analysis code next to the methodology section and say whether they agree.
- Check numbers quoted in the abstract and conclusion against the results tables, and report
  the mismatch without deciding which one is right.
- When you quote from a compiled PDF, say so, because a student searching their `.tex` will not find
  the sentence and may wrongly conclude you invented it.

## Counting

`count.py` counts characters and standard pages. Use it rather than counting yourself, and
pass on its caveats, including that PDF numbers are approximate and that LaTeX source length
is not rendered length. Never assert a character count you produced by estimation.

## Heavier reviews

`advanced.md` describes running `mad-research` or `paper-workshop` on a thesis. Neither has
been tried on one, both are calibrated for journal papers, and paper-workshop must never be
allowed to rewrite a student's thesis. Do not start either without the student asking for it
by name and understanding the cost.
