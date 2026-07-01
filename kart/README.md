# SuperTuxKart agent baseline

Starter for **SuperTuxKart Grand Prix** ([#169](https://ml-arena.com/viewcompetition/169)) —
head-to-head 4-kart racing, ranked by **ELO**.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ml-arena/competition-baseline/blob/main/kart/agent_baseline.ipynb)

**Contract** — the env owns the race loop and calls `act` once per kart per step (2 s budget):

```python
class Agent:
    def __init__(self): ...
    def act(self, obs: dict) -> dict:
        # obs: egocentric dict (velocity, front, center_path, paths, karts, items, powerup, ...)
        # return {"steer": -1..1, "acceleration": 0..1,
        #         "brake": 0/1, "drift": 0/1, "nitro": 0/1, "fire": 0/1, "rescue": 0/1}
        ...
```

Unlike the random templates this baseline actually **drives**: it steers toward the nearest
path segment ahead, drifts on sharp turns, and fires power-ups. Improve `act` (use the other
karts/items, look further ahead) or train a policy offline and upload the weights.
