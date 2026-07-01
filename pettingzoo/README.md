# PettingZoo agent baseline

Generic starter for **multi-agent** competitions on ml-arena
(Connect-Four, Chess, Texas Hold'em, the PettingZoo Atari suite, …).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ml-arena/competition-baseline/blob/main/pettingzoo/agent_baseline.ipynb)

**Contract:**

```python
class Agent:
    def __init__(self, observation_space, action_space): ...
    def reset(self, env_player_name, episode_index): ...   # optional: your seat this episode
    def choose_action(self, observation, reward=0.0, terminated=False,
                      truncated=False, info=None, action_mask=None): ...
```

For turn-based board games the observation carries an **`action_mask`** (0/1 over actions).
You **must** return an action where the mask is `1` — an illegal move forfeits the game.
The template picks a random *legal* move; replace it with search (minimax/MCTS) or a
self-play policy.

**Use it for any PettingZoo competition:** change `COMPETITION_ID` (default `65`,
Connect Four).
