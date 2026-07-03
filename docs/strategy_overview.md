# Strategy Overview

The biotech catalyst sleeve was built around dated FDA/PDUFA events.

The core idea was simple:

1. Identify small and mid-cap biotech companies with regulatory decisions inside the competition window.
2. Estimate the upside price if the event was approved.
3. Estimate the downside price if the event received a CRL or disappointed.
4. Back out the market-implied approval probability from those two prices.
5. Compare that market-implied probability with my own internal probability estimate.
6. Only consider names where the probability gap was large enough to justify event risk.

The useful part of this framework is that it forces every trade idea into explicit assumptions:

- what is the approval scenario?
- what is the failure scenario?
- what probability is the market implying?
- why should my probability estimate be different?
- how much can I lose if the catalyst fails?
- how large should the position be before the event?

This repo focuses only on that biotech catalyst process. It does not include the industrial, energy, mining, defence, or ETF sleeve from the wider presentation.

