# Allergies (IgE profiles → skin symptoms) submission baseline

Starter for **Allergies : profils IgE et symptômes cutanés**
([#176](https://ml-arena.com/viewcompetition/176)) — the *Open Data University × ml-arena*
demo built on the [Allergen Chip Challenge](https://www.data.gouv.fr/datasets/allergen-chip-challenge/)
data (Société Française d'Allergologie / Health Data Hub, Licence Ouverte 2.0).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ml-arena/competition-baseline/blob/main/allergies/submission_baseline.ipynb)

This is a **file competition**: you upload a `submission.csv`, not an `Agent` class.
The notebook is in French (the competition is), and runs end to end — download the data,
write a **constant** submission, push it through the API, read the score.

**Contract:**

```csv
patient_id,skin_symptoms
TE0000,0.5
...
```

Exactly two columns and exactly the 639 `patient_id`s of `test.csv`; `skin_symptoms` is a
probability (only the ranking matters). Metric: **ROC AUC**, higher is better.

Reference points on this exact split: constant `0.500` · benchmark (positive-IgE count)
`0.644` · logistic regression `0.785` · gradient boosting `0.795` · random forest `0.813`
(±0.016 sampling noise on 639 patients). The last cell of the notebook has the
drop-in random-forest baseline; the competition's **Datasets** tab carries a longer
`starter.ipynb` with the full feature-engineering discussion.
