# Structural checks

Ten checks that fire on things a reader can verify from the text, plus the routing that decides
which of them apply to your thesis.

A fired check does not produce a score. It moves one of the four rubric categories to a verdict —
*defensible*, *at risk*, or *not defensible as written* — and it always prints the specific change
that would lift it. A check is a floor on scrutiny, not a judgement about your thesis.

Two consequences of that. The tool must print the lift condition every time, in the same breath as
the finding, so that a check never reads as a verdict. And every check here is written so that the
only way to satisfy it is to do the thing it asks for. There is no version of "beating" CHK-D
except running the test.

---

## Routing: six families, decided by the methods section

Do not route on the topic. Titles do not classify: *Uncertainty and House Prices: Empirical
Evidence* could be a local projection, a panel regression, or a meta-analysis.

Route on three questions asked of the draft.

1. Is there a treatment?
2. Is the target a parameter or a prediction?
3. Is a row in the data an observation, or an estimate taken from another paper?

| Route | What it covers | What "identification" means here |
|---|---|---|
| **R1 causal-micro** | DiD, IV, RDD, matching, event studies | Where the variation comes from, and why the control group is the right one |
| **R2 time-series-macro** | VAR, VECM, GVAR, local projections, cointegration | How the shocks are identified: ordering, sign restrictions, external instruments |
| **R3 financial-econometrics** | Volatility, spillovers, networks, asset pricing | Not applicable. Ask instead whether the statistical object is well defined |
| **R4 forecasting-ML** | Prediction, classification, nowcasting | Not applicable. Ask instead whether the evaluation is honest |
| **R5 meta-analysis** | Rows are estimates from other papers | Which biases in the underlying literature are corrected, and how |
| **R6 structural or descriptive** | Calibration, simulation, agent-based, measurement | What the model is disciplined by, or what the description establishes |

Asking an R3 thesis for an identification strategy is a category error, and a tool that does it
will be ignored by a third of the cohort within a week. Route first.

### Family failure modes

**R1.** Causal verbs with no named design. Selection on observables presented as a fix for
endogeneity — one opponent in the sample wrote, of a thesis claiming otherwise, *"in contrast to
what the author claims, matching does not solve endogeneity issues better than OLS!"* An
instrument whose exclusion restriction is never stated in words. Treatment timing taken as given.
No account of who is in the control group and why.

**R2.** Shock identification left implicit; one supervisor report notes the VAR description is
*"quote rudimentary, e.g. as regards the shock-identification strategy"*. Conclusions the model
cannot deliver, such as claims about time variation from a time-invariant specification.
Regressions in levels with no unit-root discussion. A lagged dependent variable in a short panel
with no mention of the resulting bias.

**R3.** Nonstationarity producing a spurious fit. Overlapping windows treated as independent.
Point metrics compared across models with no inference.

**R4.** Leakage. Tuning on the evaluation sample. No naive benchmark. Class-imbalance handling
applied before the split rather than inside the training fold.

**R5.** No search protocol. No clustering at the study level. No publication-bias battery. No
best-practice estimate.

**R6.** Calibration targets unstated. No validation moment. Description sold as explanation.

---

## The ten checks

Stages are defined in `stages.md`. Categories are Contribution, Methods, Literature and Manuscript
Form, defined verbatim in `rubric_locked.md`.

### CHK-A — no falsifiable hypothesis
**Fires when** no sentence states a directional or magnitude claim that data could refute.
Objectives do not count: "to analyse the relationship between X and Y" is a plan, not a hypothesis.
**Category:** Methods. **From:** S1.
**Lift:** state at least one hypothesis in a form that some possible result would contradict.

The proposal template already demands this and says so plainly: *"don't include vague statements
and trivial identities. Hypotheses must be testable."* This is marked against Methods rather than
Contribution because that is where referees put it; one variant of the report form asks, under
Methods, whether the hypotheses are *"clearly stated, allowing their further verification and
testing"*.

### CHK-B — causal claim with no design
**Fires when** causal language appears in the abstract, hypotheses or conclusions, and no named
design with a stated untestable assumption appears in the methods.
**Category:** Contribution and Methods. **From:** S2. Warning only at S1.
**Lift:** either name the design and the assumption it rests on, or rewrite the claim as
association. Both are acceptable. Only the mismatch is not.

### CHK-C — the only novelty is a new setting
**Fires when** the stated difference from the closest cited work is a country, a period or a
dataset label, and no sentence says why the answer could differ there.
**Category:** Contribution. **From:** S1.
**Lift:** one sentence giving a reason the answer here could plausibly differ from what is already
known. See the contribution test below.

### CHK-D — no uncertainty on the headline comparison
**Fires when** the headline result compares point quantities — RMSE, accuracy, Sharpe ratio, mean
return, R² — with no interval, test or bootstrap.
**Category:** Methods. **From:** S3.
**Lift:** report a test of the difference, or state plainly that the comparison is descriptive.

One supervisor in the sample marked a thesis down for exactly this: *"The claim of better
forecasts by ML models is not well supported since it is based on mere comparison of RMSE losses.
What we need to see… is some statistical test"*. A prize-winning thesis in the same corpus makes
RMSE comparisons throughout with no test anywhere and was given full marks. The check exists
because the referees are not consistent about it and you cannot choose your referee.

### CHK-E — a single specification
**Fires when** results appear under exactly one specification, with no alternative sample,
estimator or control set.
**Category:** Methods. **From:** S4.
**Lift:** report one alternative specification, or supply the code so the specification set can be
read directly.

### CHK-F — a named assumption with no diagnostic
**Fires when** the draft names parallel trends, stationarity, instrument exogeneity,
homoskedasticity, overdispersion or a similar assumption, and no corresponding check appears.
**Category:** Methods. **From:** S3.
**Lift:** run the diagnostic, or delete the claim that depends on the assumption.

Naming an assumption creates the expectation. An opponent asked for exactly this on a
parallel-trends claim supported only by a plot: *"This statement should be followed by a more
reliable regression-based test of the parellel trend."*

### CHK-G — a limitation named and then deferred
**Fires when** a limitation is named and explicitly put aside ("out of the scope of this thesis",
"left for future research") **and** it is the main threat to the headline claim.
**Category:** Contribution. **From:** S4.
**Lift:** attempt it, even partially, and report what happened.

Honest limitations sections are worth something; one thesis in the sample that named its threats
without addressing them still received an A. Deferring the threat that decides your result is
different. The lowest-scoring report in the sample, at 45 out of 100, describes a thesis that
promised an instrumental-variables treatment of endogeneity and delivered a two-sentence note
saying it was out of scope.

### CHK-H — hypothesis drift
**Fires when** a hypothesis from the signed proposal is absent from the thesis without explanation,
or a key construct is defined two incompatible ways.
**Category:** Methods, and Manuscript Form. **From:** S3.
**Lift:** test it, or say in one sentence why it was dropped. Dropping a hypothesis is allowed.
Dropping it silently is what gets marked.

One report records the outcome: *"No hypotheses were tested despite they were listed in the
original master's thesis proposal."*

### CHK-I — out-of-sample discipline broken (R4 only)
**Fires when** any transform is fitted on the whole sample before the split — resampling, scaling,
feature selection, imputation — or when tuning targets the evaluation sample.
**Category:** Methods. **From:** S3.
**Lift:** move every fitted transform inside the training fold, or supply the code.

This is the check that most justifies the whole approach. A prize-winning thesis in the corpus
balances its data before splitting it and then states: *"Models are tuned so that their performance
on the imbalanced testing sample is maximized."* Its opponent awarded Methods 30 out of 30 and 100
out of 100 overall. A machine finds that in one pass. An experienced referee did not.

### CHK-J — the literature review is a serial summary
**Fires when** the review is a sequence of one-paper-per-paragraph summaries with no comparative
sentence and no statement of where this thesis sits.
**Category:** Literature. **From:** S3.
**Lift:** add the sentences that put the papers into disagreement with each other, and one saying
which side your thesis lands on.

---

## The promise ledger

Separate from the ten checks and run from S3.

The tool extracts every future-tense methodological commitment in your own earlier text — the
proposal, an earlier draft, the introduction — quotes it back, and reports whether the
corresponding result exists in the current draft. Three outcomes: delivered, changed with an
explanation, or missing.

This targets the pattern that the low-scoring reports punish most consistently. It also guards
against a failure this tool could otherwise cause. Told that endogeneity is unaddressed, the
quickest response is to write the sentence announcing an instrumental-variables strategy and never
run it, which makes the thesis worse. The ledger closes that route: a promise added now is checked
at the next stage.

---

## The contribution test

Contribution is the widest-spread category in the sample and the lowest floor, at 6 out of 30.
Reports whose text calls the contribution limited or unclear average 67.8 overall against 87.2 for
the rest.

One question decides it. **Does the draft say why the answer here could differ from the answer
already known elsewhere?**

If yes, the novelty is real. If no, it is a label on the same result.

"First study for the Czech Republic" is not automatically empty. A thesis on a Czech municipal
gambling ban received 28 out of 30 for contribution while resting on exactly that claim, because
the international evidence it cited genuinely disagreed with itself and because municipalities
were banning gambling without any analysis of the consequences. The answer was not predictable,
and someone was acting on the assumption. Set against that, an opponent on a regional
meta-analysis: *"The focus on Asia is novel, I guess, but it is unclear why Asia (a huge and
diverse region) should be uniquely different from the rest of the world"*. And on a thesis whose
claim was a larger dataset: *"The first contribution – extensive dataset – doesn't in my view
constitute a significant value added for a master thesis. Moreover, the author doesn't explain how
using 'more data' improves our knowledge."*

Contribution types that count at master's level, with how each is judged:

- **A new question.** Highest ceiling, rare, and no further test needed.
- **A known question in a setting where the answer could differ.** Full credit only when the "why
  it could differ" sentence is present and has content.
- **Data you assembled.** Judged on what the data lets you answer, never on its size.
- **A method brought to a new problem.** Needs a reason the method suits this problem.
- **Replication with an extension.** Currently almost absent at IES. The tool offers it actively.
- **A meta-analysis.** A contribution in itself here, but the bias battery is the entry
  requirement, not the contribution.

The tool asks for one sentence. It does not ask for a publishable paper.

---

## Robustness, and how not to cargo-cult it

Referees raise robustness in about a fifth of reports, and in roughly half of those the complaint
is that there is none.

Minimum defensible standard by route:

- **R1, DiD:** pre-trends shown as coefficients and not only as a plot; Callaway–Sant'Anna or
  Sun–Abraham **only when adoption is staggered**; one alternative control group; a placebo or
  permutation test. **IV:** first stage with its F statistic, the exclusion restriction argued in
  words, reduced form shown. **Matching:** balance before and after, common support, the algorithm
  named, and a sentence conceding that identification rests on selection on observables.
- **R2:** unit-root and cointegration tests before any levels regression; lag-length sensitivity;
  an alternative shock ordering; subsample stability.
- **R3:** an alternative estimation window; an alternative volatility proxy; a test that the
  difference between models is real.
- **R4:** a leakage-free pipeline; a naive benchmark; Diebold–Mariano or equivalent; performance
  reported on the true class distribution.
- **R5:** at least two publication-bias estimators from different families, and clustering at the
  study level.

Three rails stop this becoming a list of things bolted on and not understood.

**The tool never names a check your data cannot run.** It has to be able to point at the variable
that makes the check possible.

**Every proposed check comes with a question you must answer in one line: what result would change
your headline conclusion?** If you cannot answer, drop the check rather than run it. A robustness
test whose outcome would not move you is decoration.

**Checks are marked diagnostic or decorative for your design, and decorative ones do not satisfy
CHK-E.** Staggered-adoption estimators on a single treatment date are decorative. Declining them
and saying why is the correct answer, and it is what the strongest thesis in the sample did.

---

## Meta-analysis

The R5 route carries its own depth: FAT-PET and PEESE, the endogenous kink, p-uniform, WAAP,
Andrews–Kasy, stem-based methods, caliper tests, RoBMA, MAIVE, Bayesian model averaging for
heterogeneity, a PRISMA flow diagram, clustering at the study level, and a best-practice estimate.

That battery is the entry requirement. One meta-analysis in the corpus runs nearly all of it and
still received a B, because the concept it was measuring was defined wrongly. Method depth does
not substitute for getting the object of study right.

Three items promote out of R5 into every route, because they concern your own results rather than
other people's: report the full set of specifications you ran rather than the ones that survived;
do not present a t-statistic near 1.96 as the finding; and fix the sample-selection rule before
looking at outcomes.

---

## Code

Never required, never scored, never executed by this tool.

Supplying it does one thing: it lets CHK-E and CHK-I lift on evidence instead of on assertion. The
tool reads the code to see where the split happens and what specifications exist. Referee reports
mention replication packages in under one percent of cases, so this is not a standard anyone is
currently holding you to. It is a way to answer two checks properly.
