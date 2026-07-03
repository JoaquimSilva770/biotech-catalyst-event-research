# Catalyst Probability Model

Each catalyst is modelled as a two-outcome event:

```text
S = current price
A = approval scenario price
F = failure / CRL scenario price
P = market-implied approval probability
P* = model approval probability
```

The market-implied probability is:

```text
P = (S - F) / (A - F)
```

The break-even approval probability can also be written in return space:

```text
breakeven p = abs(D) / (abs(U) + abs(D))
```

where:

- `U` is the upside return if approved
- `D` is the downside return if the event fails

The model probability estimate `P*` is not meant to be magic. A checklist makes the judgement explicit:

- endpoint strength
- safety
- regulatory classification
- CMC/manufacturing risk
- current standard of care

Each item is scored from 0 to 4, where lower is better. The deck logic used a baseline probability of 80%, an average score of 10, and a five percentage point probability adjustment for each point above or below that average.

The final edge is:

```text
edge = P* - P
```

That edge is only useful if the scenario prices and downside are realistic.
