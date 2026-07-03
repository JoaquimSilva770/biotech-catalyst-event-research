# Biotech Catalyst Event Research

This repo reconstructs the biotech catalyst sleeve from UK Investment Competition work in Python.

The original work was built in Excel and presented as part of a broader portfolio. This repo narrows the focus to one piece: FDA/PDUFA biotech catalysts, where the core question was whether the market-implied approval probability looked too low relative to a model-scored probability estimate.

## Research Idea

Small and mid-cap biotech names can move sharply around dated regulatory events. Each catalyst is treated as a two-scenario problem:

- approval or positive regulatory outcome
- CRL/failure or negative regulatory outcome

For each event, abnormal return is measured over the same event window used in the presentation:

```text
abnormal return = stock return - S&P 500 return
event window = close at t-1 to close at t+5
```

The deck used a 2025 sample of 15 small/mid-cap biotech FDA decisions before October:

- 12 approvals
- 3 CRLs
- observed approval rate of 80%
- approval abnormal return mean around 17.7%
- CRL abnormal return mean around -13.7%
- mean-template break-even approval probability around 43.6%

The point is not that approval probability gaps are free money. The point is that dated catalysts can be modelled explicitly, with scenario payoffs, break-even probabilities, model probability scores, and strict position sizing.

## What This Repo Shows

- event-study return cleaning
- approval vs CRL payoff summaries
- market-implied approval probability extraction
- break-even approval probability math
- checklist-based model probability estimates
- probability gap / edge calculation
- Cytokinetics-style case study reconstruction
- simple position sizing based on probability edge
- small tests for the key formulas

## Repo Structure

```text
biotech-catalyst-event-research/
  data/
    pdufa_2025_events.csv
    biotech_event_returns.csv
    biotech_price_windows.csv
    cytokinetics_case_study.csv
  docs/
    strategy_overview.md
    catalyst_probability_model.md
    event_study_method.md
    limitations.md
  notebooks/
    01_event_study_and_payoffs.ipynb
    02_probability_gap_case_study.ipynb
    03_position_sizing_sanity_checks.ipynb
  src/biotech_catalyst/
    implied_probability.py
    checklist_scoring.py
    event_payoffs.py
    position_sizing.py
    risk_metrics.py
  tests/
```

## Notebooks

1. `01_event_study_and_payoffs.ipynb`
   - loads the PDUFA event dataset
   - calculates approval and CRL payoff distributions
   - reproduces the break-even approval probability logic

2. `02_probability_gap_case_study.ipynb`
   - reconstructs the Cytokinetics-style case study
   - calculates market-implied approval probability from approval/failure prices
   - applies a checklist-based model probability estimate

3. `03_position_sizing_sanity_checks.ipynb`
   - turns probability edge into capped position sizing examples
   - compares expected return and simple risk diagnostics

## How To Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=src pytest
```

Open the notebooks:

```bash
jupyter notebook notebooks/
```

## Important Limitations

This is an educational reconstruction, not investment advice and not a live strategy.

The event sample is small, biotech payoffs are fat-tailed, and approval does not guarantee a positive share-price reaction. Market prices can embed expectations, dilution risk, launch uncertainty, label constraints, and funding risk. The checklist scores are a transparent way to structure judgement, not a statistically proven probability model.
