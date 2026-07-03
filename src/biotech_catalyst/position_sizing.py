"""Simple sizing rules for probability-gap catalyst trades."""

from __future__ import annotations

from biotech_catalyst.implied_probability import clip_probability, expected_value, probability_edge


def expected_return_from_scenarios(
    current_price: float,
    approval_price: float,
    failure_price: float,
    model_probability: float,
) -> float:
    """Expected return from current price using model catalyst probability."""

    ev = expected_value(model_probability, approval_price, failure_price)
    return ev / float(current_price) - 1.0


def edge_scaled_weight(
    model_probability: float,
    implied_probability: float,
    neutral_band: float = 0.05,
    max_weight: float = 0.10,
) -> float:
    """Turn probability edge into a capped long-only position weight.

    This is intentionally simple: no position is taken inside the neutral band,
    and size increases linearly until it reaches the maximum weight.
    """

    edge = probability_edge(model_probability, implied_probability)
    if edge <= neutral_band:
        return 0.0
    usable_edge = (edge - neutral_band) / (1.0 - neutral_band)
    return min(float(max_weight), float(max_weight) * usable_edge)


def capped_weight(raw_weight: float, cap: float = 0.10) -> float:
    """Apply a single-name position cap."""

    return min(max(float(raw_weight), 0.0), float(cap))


def kelly_fraction_binary(
    approval_probability: float,
    upside_return: float,
    downside_return: float,
) -> float:
    """A rough binary Kelly fraction for a catalyst payoff.

    This is included as a diagnostic, not as a recommended sizing rule.
    """

    p = clip_probability(approval_probability)
    gain = float(upside_return)
    loss = abs(float(downside_return))
    if gain <= 0 or loss <= 0:
        raise ValueError("upside_return must be positive and downside_return must be negative")
    fraction = (p / loss) - ((1.0 - p) / gain)
    return max(0.0, fraction)
