# Paris Temperature Forecast baseline

Starter for **Paris Temperature Forecast** ([#203](https://ml-arena.com/viewchallenge/203)):
every 6 hours your agent gets the last 72 hours of weather in 45 European cities and
returns plausible Paris temperatures 6 h and 48 h later, scored with the CRPS (°C,
lower is better) once those hours have happened.

| Notebook | | Open in Colab |
|---|---|---|
| `agent_baseline.ipynb` | load the data, train a Ridge, score it locally, submit | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ml-arena/competition-baseline/blob/main/paris_temperature/agent_baseline.ipynb) |
| `data_tour.ipynb` | a tour of the data, no account needed: cycles, upwind cities, the CRPS, baselines, the two providers | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ml-arena/competition-baseline/blob/main/paris_temperature/data_tour.ipynb) |

**Contract:**

```python
class Agent:
    def predict(self, rows):
        df = pd.DataFrame(rows)    # 72 h x 45 cities, the CSV's columns
        return {"t+6h": [...], "t+48h": [...]}    # 1 to 100 temperatures each
```

**Data** (`data/`, same 13 columns, contiguous hours, `pd.concat` them):

- `weather_europe_2020_2026.csv.gz`: hourly, 2020-01-01 → 2026-03-03 UTC, Open-Meteo archive.
- `weather_europe_live_2026-03-04_2026-11-04.csv.gz`: the live feed the challenge is
  scored on (OpenWeatherMap) since then.

Reference points (mean CRPS, 2025-01 → 2026-03): last value `2.986` · climatology `2.189`
· starter agent `1.821` · Ridge (the notebook) `1.354` · gradient boosting `1.262`.
