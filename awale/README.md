# Awalé baseline

Starter for **Awalé** ([#226](https://ml-arena.com/challenges/awale)): the two-player
sowing game (12 pits, 48 seeds). Your agent picks the pit to play; it is matched against
the other participants' agents and ranked by Elo. Entry level: lists, a dictionary, one
class.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ml-arena/competition-baseline/blob/main/awale/agent_baseline.ipynb)

**Contract:**

```python
import random

class Agent:
    def choose_move(self, state):
        # state["my_pits"], state["opponent_pits"]: 6 seed counts each
        # state["my_score"], state["opponent_score"], state["legal_moves"],
        # state["time_left"], state["move_number"]
        return random.choice(state["legal_moves"])   # a pit number, 0 to 5
```

**Time:** each player has a clock of 10 seconds for all their moves of one game (clock at
zero: that game is lost), and one call may never take more than 2 seconds.

**`awale.py`** is the rules file the platform referees with. Use it to play games locally
(`awale.play_match(Agent(), awale.RandomAgent())`), and submit it next to `agent.py` when
your agent looks ahead with `awale.sow(my_pits, opponent_pits, move)`.
