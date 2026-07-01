# competition-baseline

Minimal, runnable starter notebooks for [ml-arena.com](https://ml-arena.com) competitions.
Each notebook defines a tiny `Agent`, deploys it through the [`mlarena` SDK](https://pypi.org/project/mlarena-sdk/),
and shows the leaderboard — so you always have something that runs end-to-end before you
start improving it.

Open any notebook in Colab, paste your API token (Profile → **API Keys**), set
`COMPETITION_ID`, and run top to bottom.

| Family | Covers | Contract | Open in Colab |
|--------|--------|----------|---------------|
| **Gymnasium** (single-agent RL) | LunarLander, CartPole, the Atari suite, MuJoCo control | `Agent(obs_space, act_space).choose_action(...)` | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ml-arena/competition-baseline/blob/main/gymnasium/agent_baseline.ipynb) |
| **PettingZoo** (multi-agent) | Connect-Four, Chess, Texas Hold'em, PettingZoo Atari | `Agent(...).choose_action(..., action_mask)` | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ml-arena/competition-baseline/blob/main/pettingzoo/agent_baseline.ipynb) |
| **GSM8K** (LLM reasoning) | [#165](https://ml-arena.com/viewcompetition/165) | `Agent().answer(questions) -> (solutions, traces)` | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ml-arena/competition-baseline/blob/main/gsm8k/agent_baseline.ipynb) |
| **Permuted MNIST** (1-min supervised) | [#8](https://ml-arena.com/viewcompetition/8) | `Agent().train(X, y)` + `predict(X) -> list` | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ml-arena/competition-baseline/blob/main/permuted_mnist/agent_baseline.ipynb) |
| **SuperTuxKart** (real-time racing) | [#169](https://ml-arena.com/viewcompetition/169) | `Agent().act(obs) -> action` | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ml-arena/competition-baseline/blob/main/kart/agent_baseline.ipynb) |

The **Gymnasium** and **PettingZoo** notebooks are generic templates — they work for every
competition of that kind, you only change `COMPETITION_ID` (find it in the competition-page
URL). The **GSM8K** and **Permuted MNIST** notebooks target one competition each.

## Submitting from anywhere

```python
import mlarena
client = mlarena.connect(api_key="mlk_user_…")   # Profile -> API Keys

# RL / flex competitions: put your `Agent` class in agent.py and upload it
# (uploading the file keeps its imports; the notebooks do this with %%writefile).
client.submit(competition_id=43, files=["agent.py"])

# File competitions: upload your submission file.
client.submit(competition_id=172, files=["submission.csv"])
```

See the [SDK docs](https://pypi.org/project/mlarena-sdk/) for status polling, log streaming,
runtime selection, and reading leaderboards.
