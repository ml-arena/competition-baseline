# GSM8K agent baseline

Starter for the **GSM8K** math word-problem competition
([#165](https://ml-arena.com/viewcompetition/165)).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ml-arena/competition-baseline/blob/main/gsm8k/agent_baseline.ipynb)

**Contract** — the environment sends batches of 10 questions with a 60-second timeout:

```python
class Agent:
    def __init__(self): ...
    def answer(self, questions: list[str]) -> tuple[list[float], list[str]]:
        # return (solutions, thinking_traces), one entry per question, in order
        ...
```

A reply is correct when `abs(solution - gold) < 1e-6`.

The template guesses random numbers so you can see the submit loop. The real baseline loads
a small **pre-cached** instruct model (e.g. `Qwen/Qwen2.5-0.5B-Instruct`), prompts it to
reason step by step ending in `#### <number>`, and regexes out the final number — batching
all 10 questions in one `generate` call to fit the timeout. Submit on a GPU runtime:
`client.submit(165, files=["agent.py"], runtime={"language": "python", "framework": "torch"})`.
