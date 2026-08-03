# Stages

Two different things get confused here, so the tool keeps them apart.

**The milestone** is a date. Which of the six seminars you are sitting in.

**The stage** is what you have written. The tool calibrates against this, because two students at
the same seminar can hand over a finished thesis and a paragraph.

---

## The five stages

| | Stage | What you have |
|---|---|---|
| **S0** | Idea | A topic and some reading. No structured proposal. Under about two pages. |
| **S1** | Proposal | The signed template: question, three hypotheses, a test plan for each, a named data source, a contribution claim, five references. |
| **S2** | Partial draft | Introduction, literature, data, methods, summary statistics. No results yet. This is the fifteen-page gate. |
| **S3** | Results draft | Results exist. The thesis does not yet hold together. |
| **S4** | Submission candidate | A complete thesis you would defend. |

You declare a stage. The tool reads what you actually pasted and overrides the declaration when
the two disagree, then says it did so and reviews at the stage your content is really at. This is
not a penalty. A draft is never marked down for missing something a later stage would add; the
tool tells you separately what the next stage needs.

---

## How the milestones map

The mapping is what the course expects, not a rule about what you must have.

| Milestone | Expected stage |
|---|---|
| JEM001-1, proposal defence | S1 |
| JEM001-2, methodology | S1 to S2 |
| JEM001-3, first part | S2 |
| JEM002-1, methodology and progress | S2 to S3 |
| JEM002-2, results | S3 |
| JEM002-3, defence walk-through | S4 |

**When your card says one thing and your draft says another, the tool prints it at the top of the
output.** A student at JEM002-1 whose content is still S1 has a schedule problem that no amount of
feedback on the text will fix, and it is worth hearing in August rather than in April. This is the
single cheapest diagnostic in the tool, and it is the one your instructor can act on by scanning
the card header before you stand up.

---

## Why the ladder is not the ERC ladder

This tool is modelled on the ERC pre-review, but one thing does not carry over.

The ERC stages are three different documents. Here, S2 through S4 are the same document getting
longer. That matters, because a model that has read your draft three times stops catching problems
and starts agreeing with you. The ERC package warns about this and answers it with an iteration
limit.

The answer here is different, and it is the card. The design review requires your previous card as
input. If you supply one and nothing has moved, the tool refuses to generate new findings and
re-checks the items already open instead, marking each closed, partly addressed, or unaddressed.
You cannot polish in a loop, because the tool's memory is a document you have to update by hand.

The form sweep in `basic/prompt_form_sweep.md` has no such limit. Run it as often as you like; it
cannot talk itself into a worse thesis.

---

## Which checks apply when

Full triggers are in `caps.md`. In outline:

At **S0** nothing is scored. The tool asks whether there is a question, and applies the one test
that decides Contribution: is there a reason the answer here could differ from the answer already
known elsewhere.

At **S1** the proposal template is a hard specification and the tool checks against it directly:
three hypotheses that data could refute, a test plan attached to each one, a named data source, a
contribution claim that survives the test above, five references. A causal claim with no design
gets flagged as a warning about what S2 will demand, not as a failure now.

From **S2** the design checks bind, because the methods section exists.

From **S3** the checks that need results bind: uncertainty on the headline comparison, diagnostics
for assumptions the draft names, out-of-sample discipline, and the promise ledger, which takes
every future-tense methodological commitment in your own earlier text and asks where the
corresponding result is.

At **S4** everything binds, including the checks on a single specification and on a limitation
that is named and then deferred.
