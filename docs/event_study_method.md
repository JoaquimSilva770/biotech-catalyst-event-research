# Event Study Method

The event study uses the same structure as the presentation:

```text
event window = t-1 close to t+5 close
abnormal return = stock return - S&P 500 return
```

The sample file contains 15 2025 FDA/PDUFA events before October:

- 12 approvals
- 3 CRLs

This is a small sample, so the analysis reports both mean and median payoff assumptions. That matters because biotech returns can be extremely skewed. One large approval can pull the mean far above the median, while a single disappointing label detail can turn an approval into a negative stock reaction.

The event study is used to calibrate scenario templates, not to prove a permanent statistical edge.
