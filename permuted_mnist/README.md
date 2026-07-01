# 1-Minute Permuted MNIST agent baseline

Starter for **1-Minute Permuted MNIST**
([#8](https://ml-arena.com/viewcompetition/8)).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ml-arena/competition-baseline/blob/main/permuted_mnist/agent_baseline.ipynb)

Each episode you get 60,000 labelled + 10,000 unlabelled images with **pixels and labels
randomly permuted**, and **1 minute on CPU** to train and predict. Score = test accuracy.

**Contract:**

```python
class Agent:
    def __init__(self, output_dim=10, seed=0): ...      # must work with no args
    def train(self, X_train, y_train): ...              # data arrives as lists -> np.asarray
    def predict(self, X_test) -> list: ...              # return a JSON-serializable list of ints
```

The template predicts random labels. Because pixels are permuted, convnets don't help and
you must learn from the labelled set every episode — a `LogisticRegression` / small MLP on
flattened, normalized pixels trains well inside the minute. See the notebook's final cell
for a drop-in `sklearn` baseline.
