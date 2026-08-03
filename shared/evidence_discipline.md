# Evidence discipline

The rules the tool follows when it makes a claim about your draft, and the rule you follow when
you read one.

Adapted from `tjhavranek/erc-ai-feedback`, which uses the same mechanism for ERC proposals.

---

## Every finding carries seven things

1. **A verbatim quote from your draft.** If the problem is something missing, the tool quotes the
   sentence that creates the expectation instead, and labels the finding an omission.
2. **A locator.** Section, page, table number, whatever structure your draft uses.
3. **The rubric category** it affects: Contribution, Methods, Literature or Manuscript Form.
4. **A type:** misstatement, omission, or speculative.
5. **A severity:** high, medium or low. High means an opponent would raise it as a reason not to
   recommend the current draft. Medium means it costs you standing in one category. Low means fix
   it if it is cheap.
6. **A concrete repair.** What to add, cut or reframe. Never the replacement text itself.
7. **Would an experienced referee catch this in sixty seconds?** Yes means the tool is doing its
   job, clearing something that would otherwise consume human attention. No means it is reaching,
   and the finding is marked speculative.

---

## The rule you enforce

**If you cannot find the quoted sentence in your own draft, the finding is void.**

Search for it. If it is not there, the model invented it, and everything built on it is worthless.
Discard it and report it, so the prompt can be fixed. A fabricated quote is the one failure that
blocks a release of this tool.

This rule is yours to apply, not the tool's, because the tool cannot detect its own fabrication.
It takes ten seconds and it is the only thing standing between you and a confidently wrong
critique.

---

## What the tool will not do

**It will not write your content.** Not a hypothesis, not a paragraph, not a justification, not a
sentence of your literature review. It says what is wrong and what kind of thing would fix it.
Asking it to draft the fix in the same session gets a refusal.

You can obviously open another window and ask a different model to write the paragraph. Nobody is
pretending otherwise. But you will stand in front of an opponent who asks why you chose that
specification, and the reports this tool was calibrated on end with questions like *"Provide
information about the shock identification strategy that you used in your VAR analysis, and
justify your choice"* and *"When does the bias in the FE model converge to zero?"* Text you did not
think through is text you cannot defend out loud.

**It will not produce a number, a table, or a summary statistic.** Not even a plausible-looking
one. The fifteen-page milestone exists partly to establish that you have your data; a fabricated
descriptive table defeats the one check in the course that verifies it.

**It will not give you a score or a grade.** See `rubric_locked.md` for why.

**It will not simulate a named referee.** Both reports on every defended thesis are public, so
building a model of a specific colleague's marking behaviour is technically easy. The tool refuses.
Ask it to predict what a particular person will say and it declines.

**It will not invent findings to fill space.** If your draft has few serious problems, it says so
and stops. Severity describes your draft, not a quota.

---

## When the tool and a human disagree

The human wins. That is the whole point of having a supervisor.

Two specifics worth knowing.

**The tool is calibrated to the opponent, and the opponent is the harsher reader.** Across the
sample this was built from, supervisors award 6.9 points more than opponents on the same theses.
So the tool will sometimes take a harder line than your supervisor, systematically rather than by
accident. It is not predicting your supervisor's assessment and does not claim to.

**When the tool contradicts your supervisor, that is a seminar item, not an email thread.** Put it
in section 3 of your card as an A-or-B and get it ruled on in forty seconds. Three instructors can
absorb that. They cannot absorb three hundred email threads.

**A finding that appears in one run and not the next is a candidate for a human, not a fact.**
Model output varies. Instability is a signal that the point is genuinely arguable.
