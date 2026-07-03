"""Small risk metrics used in the biotech catalyst notebooks."""

from __future__ import annotations

import numpy as np
import pandas as pd


def historical_var(returns: pd.Series, confidence: float = 0.95) -> float:
    """Historical value-at-risk as a positive loss number."""

    clean = pd.Series(returns).dropna()
    if clean.empty:
        raise ValueError("returns cannot be empty")
    return float(-np.quantile(clean, 1.0 - confidence))


def max_drawdown(cumulative_returns: pd.Series) -> float:
    """Maximum drawdown of a cumulative return path."""

    path = pd.Series(cumulative_returns).dropna()
    if path.empty:
        raise ValueError("cumulative_returns cannot be empty")
    running_max = path.cummax()
    drawdown = path / running_max - 1.0
    return float(drawdown.min())

