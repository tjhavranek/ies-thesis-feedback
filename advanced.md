# Advanced mode: use a coding agent

**Strongly recommended.** If you are writing a thesis in economics, install
[Claude Code](https://claude.com/claude-code) or
[Codex](https://developers.openai.com/codex/cli) — and ideally both. It is worth the hour it
takes to set up.

You do not need to be a programmer. You open a terminal in the folder where your thesis lives
and talk to it in English.

## Why this is better than a chatbot, not just fancier

**It reads your actual files.** Your `.tex` or `.docx`, your `.bib`, your tables, your R or
Stata code — all together, as they really are. Nothing is lost to copying and pasting, and
nothing is left out because you forgot to include it.

**It can read your code against your text.** Ask it whether your analysis code does what your
methodology section claims. This is the single most valuable thing on this page: a chatbot
can only do it if you paste the code in as well, your supervisor rarely has time to, and the gap between what students say they did and
what their code actually does is where real problems hide. It needs your project folder, with
the `.do` or `.R` files sitting alongside the draft — a compiled PDF on its own is not enough.

**It checks its own quotations.** Before it shows you anything, it can go back to your files
and confirm that every sentence it quoted is really there. A chatbot cannot, which is why
chatbots sometimes quote things you never wrote.

**It can look things up.** Whether the paper you are citing says what you think it says,
whether a method is still considered sound, what the current literature actually concluded.

## Why both, if you can

Claude Code and Codex are different models from different companies. Run the same question
past both and you will get two different readings, and **the places where they disagree are
the places worth your attention**. Where they agree, you can move on. This is the cheapest
form of a second opinion you will ever get, and it is the same logic as sending a paper to two
referees.

If you can only have one, either is fine. Do not agonise over the choice.

## What it costs

Both need a paid subscription, at roughly the price of a textbook per month. Claude Code comes
with a Claude subscription; Codex comes with a ChatGPT subscription. Many students already pay
for one of these, in which case the agent is included and you simply have not installed it yet.

If money is genuinely tight, the [basic mode](README.md) on a free chatbot is a real tool and
not a consolation prize. Use it without embarrassment.

## How to use it on your thesis

Install the agent, then clone this repository and open the agent in its folder:

```
git clone https://github.com/tjhavranek/ies-thesis-feedback
cd ies-thesis-feedback
```

Then just ask, in plain English:

```
check my thesis in ../my-thesis
```

`AGENTS.md` tells the agent what to do: read `prompt.md`, follow it, read your files rather
than asking you to paste them, verify every quotation against your text, and change nothing.
Codex reads that file on its own. Claude Code looks for `CLAUDE.md` instead, so the repository
carries a one-line `CLAUDE.md` that points at it. If you are not sure it loaded, just say
"read AGENTS.md and follow it" as your first message.

Three things worth asking for specifically:

- "Does my code do what my methodology section says it does?"
- "Check every number in my abstract and conclusion against my results tables."
- "Which entries in my `.bib` do I never actually cite, and which citations are missing from
  it?"

**It must not edit your thesis.** If the agent offers to fix something, say no. You make the
changes, because you are the one who will be asked about them at the defence.

## Two heavier reviews, with a warning

Two of my other repositories run much deeper adversarial reviews:

- **[mad-research](https://github.com/tjhavranek/mad-research)** — Claude and Codex argue about
  a document and a third pass adjudicates.
- **[paper-workshop](https://github.com/tjhavranek/paper-workshop)** — a workshop of referees
  from competing traditions, every comment tied to a quotation.

Both were built for research papers heading to journals. **Neither has been tried on a
master's thesis**, there is no evidence either gives better advice than one careful pass with
`prompt.md`, and both are slow and cost real money in tokens.

If you use them anyway: run them on a near-final draft, not an early one. **Never let
paper-workshop rewrite your thesis** — it has a mode that produces a revised version, which is
built for an author revising their own paper and would take the writing out of your hands. Use
the criticism; write the fix yourself. And remember both are calibrated for publication, so
they will ask for things no examiner expects. Your supervisor decides what is worth doing.

## What does not change

Everything in `prompt.md` still applies. No agent writes your thesis, invents numbers, gives
you a grade, or guesses a deadline. If one quotes a sentence that is not in your text, that
finding is worthless — discard it and please open an issue.

Using any of this counts as AI use that you declare in the thesis. See
[`reference.md`](reference.md).
