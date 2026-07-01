# Gymnasium agent baseline

Generic starter for **single-agent Gymnasium** competitions on ml-arena
(LunarLander, CartPole, the Atari suite, MuJoCo control, …).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ml-arena/competition-baseline/blob/main/gymnasium/agent_baseline.ipynb)

**Contract** — the worker imports `Agent` from your `agent.py` and runs it:

```python
class Agent:
    def __init__(self, observation_space, action_space): ...
    def choose_action(self, observation, reward=0.0, terminated=False,
                      truncated=False, info=None, action_mask=None): ...
```

Return an action drawn from `action_space`; return `None` when `terminated`/`truncated`.
The template plays random actions — replace `choose_action` with your trained policy.

**Use it for any single-agent competition:** just change `COMPETITION_ID` in the notebook
(the id is in the competition-page URL). Default is `43` (LunarLander-v3).
