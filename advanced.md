# Advanced mode

For students who already use an agent — Claude Code, Codex CLI, or similar. If you do not,
**use the [basic mode](README.md) instead**; it is the main route and it is not a lesser
version. Almost everyone should use it.

What you get here that a chatbot cannot give you: the agent reads your actual files, so it
sees your LaTeX source, your tables, your `.bib` and your code together, and it checks its own
quotations against your text before showing you anything.

---

## The basic agentic run

Clone this repository and open your agent in the folder, then ask it to look at your thesis:

```
check my thesis in ../my-thesis
```

`AGENTS.md` in this repository tells the agent what to do, and it amounts to: read
`prompt.md`, follow it, read your files rather than asking you to paste them, verify every
quotation against your source before printing, and change nothing.

**It must not edit your thesis.** If your agent offers to fix something, say no. The point of
the exercise is that you make the changes, because you are the one who will be asked about
them.

Three things worth doing that the chatbot route cannot:

- Give it your `.tex` and your `.bib` together, so it can see which references you actually
  cite.
- Give it your analysis code alongside the draft, and ask whether the code does what the
  methodology section says it does. This catches real problems and no chatbot can do it.
- Ask it to check the numbers in your abstract and conclusion against your results tables.

## Two heavier tools, and an honest warning

Two of my other repositories run much deeper adversarial reviews:

- **[mad-research](https://github.com/tjhavranek/mad-research)** — an audit where Claude and
  Codex argue about a document and a third pass adjudicates.
- **[paper-workshop](https://github.com/tjhavranek/paper-workshop)** — a workshop of referees
  from competing traditions, every comment tied to a quotation.

Both were built for research papers heading to journals, **neither has been tried on a
master's thesis**, and there is no evidence that either gives better advice than one careful
pass with `prompt.md`. They are slow and they cost real money in tokens.

If you use them anyway:

- Run them on a **near-final draft**. On an early draft they will bury you in problems you
  already know about.
- **Never let paper-workshop rewrite your thesis.** It has a mode that produces a revised
  version with tracked changes. That is built for an author revising their own paper, and for
  a thesis it takes the writing out of your hands. Use the criticism, write the fix yourself.
- Remember that both are calibrated for publication, not for a master's thesis. They will ask
  for things no examiner expects. Read their output as an argument to weigh, not a checklist.
  Your supervisor decides what is worth doing.

## What does not change

Everything in `prompt.md` still applies. No agent should write your thesis, invent numbers,
give you a grade, or guess a deadline. If an agent quotes a sentence that is not in your text,
that finding is worthless — discard it and please open an issue.

Your use of any of this counts as AI use that you declare in the thesis. See
[`reference.md`](reference.md).
