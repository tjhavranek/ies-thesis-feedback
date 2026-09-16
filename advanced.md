# Advanced mode: use a coding agent

**Strongly recommended.** If you are writing a thesis in economics, install
[Claude Code](https://claude.com/claude-code) or
[Codex](https://developers.openai.com/codex/cli), and ideally both. Setting one up takes about an hour.

You do not need to program. You open a terminal in your thesis folder and type what you want in English.

## What an agent does that a chatbot does not

**It reads your files.** Your `.tex` or `.docx`, your `.bib`, your tables and your R or Stata code, all at once and as they are. Nothing is lost to copying and pasting, and
nothing is left out because you forgot to include it.

**It can read your code against your text.** Ask it whether your analysis code does what your
methodology section claims. This is the main reason to use an agent. A chatbot can do it only if you paste the code in as well, supervisors rarely have time to, and serious problems turn up in the gap between what students say they did and what the code does. It needs your project folder, with the `.do` or `.R` files next to the draft. A compiled PDF on its own is not enough.

**It checks its own quotations.** Before it shows you anything, it can go back to your files
and confirm that every sentence it quoted is there. A chatbot cannot, which is why
chatbots sometimes quote things you never wrote.

**It can look things up.** Whether the paper you are citing says what you think it says,
whether a method is still considered sound, what the current literature concluded.

## Why both, if you can

Claude Code and Codex are different models from different companies. Run the same question
past both and you will get two different readings. **Look hardest at the points where they disagree.** Where they agree, you can move on. This is the cheapest
form of a second opinion you will ever get, and it is the same logic as sending a paper to two
referees.

If you can only have one, either is fine. Do not agonise over the choice.

## What it costs

Both need a paid subscription, at roughly the price of a textbook per month. Claude Code comes
with a Claude subscription; Codex comes with a ChatGPT subscription. Many students already pay
for one of these, in which case you already have the agent and only need to install it.

If money is tight, use the [basic mode](README.md) on a free chatbot. It runs the same review prompt.

## How to use it on your thesis

Install the agent, then clone this repository and open the agent in its folder:

```
git clone https://github.com/tjhavranek/ies-thesis-feedback
cd ies-thesis-feedback
```

Then ask, in plain English:

```
check my thesis in ../my-thesis
```

`AGENTS.md` tells the agent what to do: read `prompt.md`, follow it, read your files rather
than asking you to paste them, verify every quotation against your text, and change nothing.
Codex reads that file on its own. Claude Code looks for `CLAUDE.md` instead, so the repository
carries a one-line `CLAUDE.md` that points at it. If you are not sure it loaded, say
"read AGENTS.md and follow it" as your first message.

Three useful requests:

- "Does my code do what my methodology section says it does?"
- "Check every number in my abstract and conclusion against my results tables."
- "Which entries in my `.bib` do I never cite, and which citations are missing from
  it?"

**It must not edit your thesis.** If the agent offers to fix something, say no. You make the
changes, because you are the one who will be asked about them at the defence.

## Two heavier reviews, with a warning

Two other repositories by the same author run much deeper adversarial reviews:

- [mad-research](https://github.com/tjhavranek/mad-research): Claude and Codex argue about
  a document and a third pass adjudicates.
- [paper-workshop](https://github.com/tjhavranek/paper-workshop): a workshop of referees
  from competing traditions, every comment tied to a quotation.

Both were built for research papers heading to journals. **Neither has been tried on a
master's thesis**, there is no evidence either gives better advice than one careful pass with
`prompt.md`, and both are slow and cost money in tokens.

If you use them anyway: run them on a near-final draft, not an early one. **Never let paper-workshop rewrite your thesis.** It has a mode that produces a revised version, which is
built for an author revising their own paper and would take the writing out of your hands. Use
the criticism; write the fix yourself. And remember both are calibrated for publication, so
they will ask for things no examiner expects. Your supervisor decides which of their points to act on.

## What does not change

Everything in `prompt.md` still applies. No agent writes your thesis, invents numbers, gives
you a grade, or guesses a deadline. If one quotes a sentence that is not in your text, that finding is worthless. Discard it and please open an issue.

Using any of this counts as AI use that you declare in the thesis. See
[`reference.md`](reference.md).
