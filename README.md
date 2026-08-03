# ies-thesis-feedback

A set of prompts for students writing a master's thesis at the Institute of Economic Studies,
Charles University. You paste one into a chat with a current model, along with your draft, and it
reads your work the way your opponent will.

It is built for the two thesis seminars, JEM001 and JEM002, and it covers every stage from having
an idea to the week before you submit.

It does not replace your supervisor. It clears the problems that a supervisor should not have to
spend time on, so that the time you get with one goes on the judgement only they can supply.

---

## Start here

| You have | Use |
|---|---|
| A topic and no proposal | [`basic/prompt_idea.md`](basic/prompt_idea.md) |
| A proposal or a draft | [`basic/prompt_review.md`](basic/prompt_review.md) |
| Anything, at any time | [`basic/prompt_form_sweep.md`](basic/prompt_form_sweep.md) |

Before the design review, fill in a [Seminar Card](shared/card.md). It takes twenty minutes and it
is what the tool reads first.

Read [`docs/privacy.md`](docs/privacy.md) before you paste an unpublished draft anywhere.

---

## What it does

**It reads as the opponent.** Your thesis gets two reports. Across 230 filed reports at this
institute, supervisors award about seven points more than opponents on the same thesis. The
opponent is the binding reader, so that is who this simulates. It says so in its own output, and
it is not predicting what your supervisor will write.

**It routes on your design before it says anything.** A volatility-spillover thesis has no
identification strategy, and asking it for one is a category error. Six routes — causal
microeconometrics, macro time series, financial econometrics, forecasting and machine learning,
meta-analysis, structural and descriptive — each with its own failure modes.

**It runs ten structural checks** that fire on things anyone can verify in the text: a causal claim
with no design, a hypothesis nothing could refute, a contribution that is only a new country, a
headline comparison with no test, an assumption named but never checked, a promise from the
proposal that the thesis never delivers. Full list in [`shared/caps.md`](shared/caps.md).

**It asks before it tells.** Section 2 of your card is your own statement of the main threat to
your design and what you did about it. Leave it blank and the tool will not discuss your
identification at all; it returns the questions you need to answer instead. The gap between your
answer and its answer is the part worth reading.

**It quotes.** Every finding carries a verbatim sentence from your draft. If you cannot find that
sentence in your own file, the finding is void. Discard it and report it.

## What it will not do

It will not write any part of your thesis. It will not produce a number, a table or a summary
statistic, even as an illustration. It will not give you a score, points or a predicted grade at
any stage. It will not model or predict a named referee. It will not help you declare less AI use
than you made.

The refusal to write your content is not enforceable and nobody pretends it is; you can open
another window. But you will stand in front of someone who asks why you chose that specification.
The reports this was calibrated on end with questions like *"Provide information about the shock
identification strategy that you used in your VAR analysis, and justify your choice."* Text you
did not think through is text you cannot defend out loud.

## Why there is no predicted grade

The real form is filled inconsistently. One report in the sample awards 30 points in a box whose
maximum is 20 and totals it at 99 anyway. Referees disagree sharply with each other: one thesis
was marked down for comparing forecast errors with no statistical test while another doing the same
thing received full marks. Half of all reports recommend an A, so a good grade is weak evidence of
a good thesis.

A number built on that would be noise, and a number is the kind of thing students optimise
against. So the tool gives verdicts and repairs: for each of the four rubric categories, whether
the draft is defensible, at risk, or not defensible as written, and what specific change would lift
it. See [`shared/rubric_locked.md`](shared/rubric_locked.md).

---

## Contents

```
shared/
  rubric_locked.md        the four IES categories, quoted from the report form
  card.md                 the Seminar Card
  stages.md               the five stages, and how they map to the six seminars
  caps.md                 design routing, the ten checks, contribution, robustness
  evidence_discipline.md  what a finding must carry, and the rule you enforce
basic/
  prompt_idea.md          before you have a proposal
  prompt_review.md        the main tool
  prompt_form_sweep.md    formatting, tables, citations, language
docs/
  ai_declaration.md       declaring AI use, and what actually protects you
  privacy.md              data rules, no-paste mode, which account to use
  for_supervisors.md      how this fits a seminar, and its limits
scripts/
  card_check.py           mechanical completeness check over a folder of cards
tests/fixtures/           synthetic drafts with planted defects, one per route
```

---

## How it was built

Calibrated against 115 IES master's theses and the 230 supervisor and opponent reports filed with
them, all published in the Charles University repository. The rubric is quoted from that form
rather than paraphrased. The distribution of scores, the gap between supervisors and opponents,
and the measured shares of referee attention are in
[`shared/rubric_locked.md`](shared/rubric_locked.md).

Two findings shaped the design more than the rest. Referees spend more of their written reports on
formatting and typos than on identification, which is why the form sweep is a separate tool you
run first and often. And an award-winning thesis in the sample states that its models were tuned to
maximise performance on the sample it then evaluates them on, and was given full marks for methods
by its opponent. A machine catches that in one pass. The point of structural checks is consistency
that human referees, reading under time pressure, do not have.

This is the thesis-seminar application of the same approach as
[`tjhavranek/erc-ai-feedback`](https://github.com/tjhavranek/erc-ai-feedback), which does this for
ERC grant proposals. Related: [`tjhavranek/paper-workshop`](https://github.com/tjhavranek/paper-workshop)
and [`tjhavranek/mad-research`](https://github.com/tjhavranek/mad-research).

## Limits

Calibrated for IES master's theses. Not for bachelor's theses, dissertations, or other faculties.

It catches structural problems. It does not judge whether your idea is interesting, and it will
confidently miss things specific to your field. Where it disagrees with your supervisor, your
supervisor wins; bring the disagreement to the seminar as a yes-or-no question.

The rubric and the course requirements change. The versions here were verified on 2026-08-03. If
you are reading this a year later, check before relying on it.

## Licence and maintenance

MIT. Developed at the Institute of Economic Studies, Charles University, for JEM001 and JEM002.

The IES report form and course materials quoted here remain the property of the Institute.

Corrections to the rubric, and any case where the tool invented a quote, belong in GitHub Issues.
A fabricated quote is a release-blocking bug; please report it. Do not paste your draft or anyone
else's into a public issue.
