# The Seminar Card

One page, filled in before you present. It is the agenda for your five minutes, and it is the only
thing this tool remembers between runs.

You can fill it in by hand. Nothing here requires you to use AI, and choosing not to costs you
nothing.

---

## Why it exists

You get about five minutes at each seminar. Today most of that goes on the instructor working out
what the state of your project is and where the weak point sits. By the time the diagnosis is
done, the time is gone, and you leave with the diagnosis rather than with a decision.

The card moves the diagnosis to your desk. You arrive having already named the main threat to your
design and having tried something about it, so the five minutes goes on the judgement you cannot
make alone.

The second field is the one that matters. An opponent report in the sample this tool was built
from says of a thesis that had a limitations section: *"[the author] shortly discusses these
limitations is a separate section, but does nothing to adress them."* Naming a threat earns
nothing. Attempting it earns everything.

---

## The card

```
=== IES THESIS SEMINAR CARD ===
STUDENT:                          SUPERVISOR:
MILESTONE:   [JEM001-1 | JEM001-2 | JEM001-3 | JEM002-1 | JEM002-2 | JEM002-3]
DATE:
DESIGN FAMILY:  [causal-micro | time-series-macro | financial-econometrics |
                 forecasting-ML | meta-analysis | structural-or-descriptive]
DATA STATUS:    [none | requested | in hand, not cleaned | analysis-ready]
AI PRE-REVIEW:  [not run | run: model ____, date ____ ]

--- 1. THE CLAIM (three sentences, no more) ---
I estimate ................................ using ................................ .
If I am right, the number tells us ................................ .
Nearest prior work: [Author Year]. What my thesis does that it does not: ................ .

--- 2. THE THREAT I CANNOT DISMISS ---
Threat, in one sentence, stated so that it could be true:
   ................................................................
Why it is a threat in my data specifically:
   ................................................................
What I DID about it (past tense; not what I plan to do):
   Attempt: ........................................................
   Result:  ........................................................
   Verdict: [threat reduced | threat survives | could not check yet because ........ ]
Where this now appears in my draft: [section / page / table]

--- 3. WHAT I WANT ADJUDICATED (at most three, each an A-or-B) ---
Q1. [A] ................ or [B] ................ ?   My lean: [A/B], because ........
Q2.
Q3.

--- 4. CARRIED FORWARD FROM MY LAST CARD ---
[item] -- [closed | partly addressed | unaddressed] -- one line on why
=== END CARD ===
```

---

## The two rules that make it work

**Section 2 takes a past-tense verb.** "I will run a placebo test" is a plan, not an attempt. If
you have not been able to check the threat yet, write `could not check yet because ...` and give
the real reason. That is still an honest, diagnosed arrival, and the reason itself becomes the
question worth asking in the room.

**Section 3 takes binary choices only.** "What do you think of my identification?" consumes the
whole five minutes and produces a conversation you could have had with anyone. "Municipality level
or district level?" is a forty-second ruling from someone qualified to make it. If a question
cannot be written as A-or-B, it is not ready for the seminar; work on it or move it to a
supervision meeting.

If you run the AI tool, it will rewrite an open question in section 3 into an A-or-B, or tell you
the question is not ready. It will not answer section 2 for you: without your own words there, it
will not comment on your identification at all. That is deliberate. The gap between what you wrote
and what the tool says is the part you learn from.

---

## Design family

Declare it yourself. The tool checks the declaration against your methods section and tells you if
they disagree, which is itself worth knowing.

The family decides which questions apply. "What is your identification strategy?" is the wrong
question for a volatility-spillover thesis, and asking a forecasting thesis about parallel trends
is a category error. Instead:

- **causal-micro** — where does the variation come from, and who is in the control group?
- **time-series-macro** — how are the shocks identified, and are the series stationary?
- **financial-econometrics** — is the statistical object well defined, and is any difference
  between models tested rather than eyeballed?
- **forecasting-ML** — is the pipeline free of leakage, and is there a benchmark?
- **meta-analysis** — what is the search protocol, and how is publication bias handled?
- **structural-or-descriptive** — what are the calibration targets, or what does the description
  establish that a reader could not assume?

---

## What section 2 asks for at each milestone

| Milestone | The attempt that counts |
|---|---|
| JEM001-1, proposal | Evidence that the variation you need actually exists in your setting |
| JEM001-2, methodology | Your identifying assumption written as a sentence that could be false, plus the check that would detect its failure |
| JEM001-3, first part | Descriptive evidence on why treatment happened where it did |
| JEM002-1, progress | Your robustness list, written down before you look at the results |
| JEM002-2, results | That same list, ticked off, including the checks that broke |
| JEM002-3, walk-through | Your own opponent report: four questions you expect, your ninety-second answers, and the one concession you will make gracefully |

The last one is the highest-value card of the six. Defence records show that the students who do
well are the ones who answered the questions in the two reports, and at least one turned on
conceding in the room that the estimates were closer to correlations than to causal effects.

---

## For a supervision meeting

Same card, plus two lines: what you need from your supervisor that nobody else can give, and what
you did about whatever you agreed last time.

---

## The AI line

`AI PRE-REVIEW` is a record, not a confession. Six dated entries across two years mean that when
you write the declaration of AI use that Charles University requires in every final thesis, you
are assembling it from something you wrote at the time rather than reconstructing it from memory.
`not run` is a normal entry. See `docs/ai_declaration.md`.
