"""Probability and payoff math for binary biotech catalyst events."""

from __future__ import annotations


def clip_probability(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    """Keep a probability inside a closed interval."""

    return max(lower, min(upper, float(value)))


def market_implied_probability(
    current_price: float,
    approval_price: float,
    failure_price: float,
) -> float:
    """Infer the approval probability implied by a two-scenario price tree.

    The setup is:

    current_price = p * approval_price + (1 - p) * failure_price

    Rearranging gives:

    p = (current_price - failure_price) / (approval_price - failure_price)
    """

    denominator = approval_price - failure_price
    if denominator == 0:
        raise ValueError("approval_price and failure_price must be different")
    return clip_probability((current_price - failure_price) / denominator)


def breakeven_probability(upside_return: float, downside_return: float) -> float:
    """Compute the approval probability needed to break even.

    Returns are expressed as decimals. For example, 0.18 means +18% and
    -0.14 means -14%.
    """

    upside = abs(float(upside_return))
    downside = abs(float(downside_return))
    denominator = upside + downside
    if denominator == 0:
        raise ValueError("upside_return and downside_return cannot both be zero")
    return downside / denominator


def scenario_prices(
    current_price: float,
    upside_return: float,
    downside_return: float,
) -> tuple[float, float]:
    """Convert return assumptions into approval and failure prices."""

    approval_price = current_price * (1.0 + upside_return)
    failure_price = current_price * (1.0 + downside_return)
    return approval_price, failure_price


def expected_value(
    model_probability: float,
    approval_price: float,
    failure_price: float,
) -> float:
    """Expected catalyst value under a model approval probability."""

    p = clip_probability(model_probability)
    return p * approval_price + (1.0 - p) * failure_price


def probability_edge(model_probability: float, implied_probability: float) -> float:
    """Difference between model probability and market-implied probability."""

    return float(model_probability) - float(implied_probability)
