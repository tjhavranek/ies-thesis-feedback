# Feedback on your thesis

*Tomáš Havránek, Charles University · methods, data and code for meta-analysis at [meta-analysis.cz](https://meta-analysis.cz)*

**The app: [tjhavranek.github.io/ies-thesis-feedback](https://tjhavranek.github.io/ies-thesis-feedback/)**

For students writing a master's thesis at the Institute of Economic Studies, Charles
University.

Send an AI chatbot whatever you have (an idea, your proposal, half a draft or a finished thesis) and get it read the way your supervisor and your opponent will read it, with
concrete suggestions for making it better.

**If you use it, use it before your seminar.** Then the time you get with an economist is spent on the
things AI cannot do: whether your question matters in this literature, whether your design
is credible, and whether you can defend what you wrote. Using it is optional, and nobody is required to use AI for their thesis.

**[Start here](https://tjhavranek.github.io/ies-thesis-feedback/).** The page has one button and needs nothing installed.

Or do it by hand: open [`prompt.md`](prompt.md), copy the text between the two markers, paste
it into a chatbot, and attach your draft after it.

Use **ChatGPT** or **Claude**. Both handle academic work well. Gemini will run the prompt, but
it is currently the weaker of the three for this, so reach for it last. A paid account reads a
long draft better than a free one; on a free account, send a chapter at a time.

## What it does

It works out what you have sent and says so, then goes through your work in this order:

- **Your question.** Is it a research question or a topic? Can it be done with data you can get?
- **Your contribution.** The one that decides how the thesis is received: does your work say
  why the answer *here* could differ from what is already known?
- **Your design.** Whether the method can support the claim. It works out what kind of
  empirical work you are doing first, so a volatility thesis is not expected to have
  an identification strategy.
- **Your results.** Robustness, uncertainty, and whether you delivered what the proposal
  promised.
- **Your writing.** Whether the abstract says what you found and the tables can be read alone.

It also tells you roughly where you should be by now, because students are often behind without knowing it.

It quotes your own sentences so you can find what it is talking about, it checks its own points
before it shows them to you and drops the ones it cannot stand behind, and it ends with two or
three questions to take to your supervisor.

## What it will not do

It will not write your thesis, produce numbers or tables, count your characters, or give you
a grade or predict one. It will not guess a deadline. It will not help anyone write a
supervisor's or opponent's report on someone else's thesis.

On grades specifically: the two reports on the same thesis routinely disagree, and in a recent
sample of filed reports half recommended an A. A predicted mark would be noise, and you would end up
improving the number instead of the thesis.

## Before you paste anything

A chatbot sends what you give it to the company that runs it. Check your supervisor is
content, and check your data licence if your data is not public. Using this counts as AI use,
which the university requires you to declare in your thesis. Declaring it is normal and is not held against you. See [`reference.md`](reference.md).

## Two modes

**Basic** is the button above: one prompt, any chatbot, nothing installed. It works, and if
this is all you ever use, that is fine.

**Advanced mode is better.** Use [Claude Code](https://claude.com/claude-code)
or [Codex](https://developers.openai.com/codex/cli), and ideally both. The desktop apps make it easy, with no terminal and no programming: Claude Code is the Code tab in the [Claude app](https://claude.com/download), and Codex comes inside the [ChatGPT app](https://chatgpt.com/download/). You open your thesis folder and write to it in plain English.

It reads the files themselves, so nothing depends on what you remembered to paste: your `.tex` or `.docx`, your
`.bib`, your tables and your analysis code, together. It can tell you **whether your code does
what your methodology section says it does**, which a chatbot can do only if you paste the code
in as well, and which is where serious problems turn up. It checks its own quotations against your text before showing you anything.

Running both helps more, because they are different models: where they disagree is where
you should look. Claude Code needs a paid Claude plan. Codex also works on a free ChatGPT
account, though with small limits. If you already pay for Claude or ChatGPT, you already have
the agent and only need to install the app.

See [`advanced.md`](advanced.md), which also covers the heavier
[mad-research](https://github.com/tjhavranek/mad-research) and
[paper-workshop](https://github.com/tjhavranek/paper-workshop) reviews, with a warning:
both were built for journal papers, neither has been tried on a thesis, and paper-workshop must
never be allowed to rewrite yours.

## Also here

- [`reference.md`](reference.md): what good looks like at each stage, the length rules,
  how the four referee headings work, and what reliably costs students marks. Read it even if you never use the prompt.
- [`count.py`](count.py): optional. Counts characters and standard pages, because a
  chatbot cannot count and you need to know whether you are near the minimum. Runs on your own
  machine, sends nothing.
- [`advanced.md`](advanced.md): the agent route.
- [`AGENTS.md`](AGENTS.md): what an agent is told to do, if you want to check.

## Limits

It is not official. Neither IES nor the faculty has endorsed it. It cannot tell you your
grade and it does not know your supervisor.

It misses things a specialist in your field would catch, and it can be wrong with confidence.
Push back when you disagree. And if it quotes a sentence that is not in what you sent it, that finding is worthless. Search a few distinctive words rather than the whole sentence, since extraction from a PDF breaks hyphenated words, and then please [open an issue](../../issues) and
say so. Do not paste
any part of a real thesis into a public issue.

Deadlines and requirements change every academic year. Take dates from the current FSV
academic calendar and your course Moodle, never from here and never from a chatbot.

## Licence

MIT (see [LICENSE](LICENSE)). The IES form and course materials quoted here remain the Institute's property ([NOTICE.md](NOTICE.md)). Built at the Institute of Economic Studies, Charles University, by Tomáš Havránek ([meta-analysis.cz](https://meta-analysis.cz)). The approach follows
[erc-ai-feedback](https://github.com/tjhavranek/erc-ai-feedback) and
[gauk-ai-feedback](https://github.com/tjhavranek/gauk-ai-feedback).
