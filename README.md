# Feedback on your thesis

For students writing a master's thesis at the Institute of Economic Studies, Charles
University.

Send an AI chatbot whatever you have — an idea, your proposal, half a draft, a finished
thesis — and get it read the way your supervisor and your opponent will read it, with
concrete suggestions for making it better.

**Use it before your seminar.** Then the time you get with an economist is spent on the
things AI cannot do: whether your question matters in this literature, whether your design
is credible, and whether you can defend what you wrote.

**→ [Start here](https://tjhavranek.github.io/ies-thesis-feedback/)** — one page, one button,
nothing to install.

Or do it by hand: open [`prompt.md`](prompt.md), copy the text between the two markers, paste
it into any chatbot, and attach your draft after it.

## What it does

It works out what you have sent and says so, then goes through your work in this order:

- **Your question.** Is it a research question or a topic? Can it be done with data you can
  actually get?
- **Your contribution.** The one that decides how the thesis is received: does your work say
  why the answer *here* could differ from what is already known?
- **Your design.** Whether the method can support the claim. It works out what kind of
  empirical work you are doing first, so a volatility thesis is not asked for an
  identification strategy.
- **Your results.** Robustness, uncertainty, and whether you delivered what the proposal
  promised.
- **Your writing.** Whether the abstract says what you found and the tables can be read alone.
- **The practical things**, briefly — length, what is due next, what the referee reports look
  at.

It quotes your own sentences so you can find what it is talking about, and it ends with two
or three questions worth taking to your supervisor.

## What it will not do

It will not write your thesis, produce numbers or tables, count your characters, or give you
a grade or predict one. It will not guess a deadline. It will not help anyone write a
supervisor's or opponent's report on someone else's thesis.

On grades specifically: the two reports on the same thesis routinely disagree, and half of
all filed reports recommend an A. A predicted mark would be noise, and you would end up
improving the number instead of the thesis.

## Before you paste anything

A chatbot sends what you give it to the company that runs it. Check your supervisor is
content, and check your data licence if your data is not public. Using this counts as AI use,
which the university requires you to declare in your thesis — declaring is normal and is not
held against you. See [`reference.md`](reference.md).

## Two modes

**Basic** is the button above: one prompt, any chatbot, nothing installed. This is the main
route and almost everyone should use it.

**Advanced** is for students who already use Claude Code, Codex CLI or a similar agent. The
agent reads your files directly, checks its quotations against your source, and can compare
your analysis code against what your methodology section claims. See
[`advanced.md`](advanced.md), which also covers running the heavier
[mad-research](https://github.com/tjhavranek/mad-research) and
[paper-workshop](https://github.com/tjhavranek/paper-workshop) reviews, with an honest warning
attached: both were built for journal papers, neither has been tried on a thesis, and
paper-workshop must never be allowed to rewrite yours.

## Also here

- **[`reference.md`](reference.md)** — what good looks like at each stage, the length rules,
  how the four referee headings work, and what reliably costs students marks. Worth ten
  minutes even if you never use the prompt.
- **[`count.py`](count.py)** — optional. Counts characters and standard pages, because a
  chatbot cannot count and you need to know whether you are near the minimum. Runs on your own
  machine, sends nothing.
- **[`advanced.md`](advanced.md)** — the agentic route.
- **[`AGENTS.md`](AGENTS.md)** — what an agent is told to do, if you want to check.

## Honest limits

It is not official. Neither IES nor the faculty has endorsed it. It cannot tell you your
grade and it does not know your supervisor.

It misses things a specialist in your field would catch, and it can be wrong with confidence.
Push back when you disagree — and if it quotes a sentence you cannot find in your own draft,
that finding is worthless, so please [open an issue](../../issues) and say so. Do not paste
any part of a real thesis into a public issue.

Deadlines and requirements change every academic year. Take dates from the current FSV
academic calendar and your course Moodle, never from here and never from a chatbot.

## Licence

MIT. Built at the Institute of Economic Studies, Charles University. The approach follows
[erc-ai-feedback](https://github.com/tjhavranek/erc-ai-feedback) and
[gauk-ai-feedback](https://github.com/tjhavranek/gauk-ai-feedback).
