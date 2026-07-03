"""Checklist scoring for internal catalyst probability estimates."""

from __future__ import annotations

from collections.abc import Mapping

from biotech_catalyst.implied_probability import clip_probability

CHECKLIST_ITEMS = (
    "endpoint_strength",
    "safety",
    "regulatory_classification",
    "cmc_risk",
    "standard_of_care",
)


def validate_score(value: float) -> float:
    """Validate one checklist score.

    The deck used scores from 0 to 4 for each item, where lower is better.
    """

    score = float(value)
    if not 0.0 <= score <= 4.0:
        raise ValueError("checklist scores must be between 0 and 4")
    return score


def score_catalyst(scores: Mapping[str, float]) -> float:
    """Sum the five checklist items into one catalyst risk score."""

    missing = [item for item in CHECKLIST_ITEMS if item not in scores]
    if missing:
        raise KeyError(f"missing checklist scores: {missing}")
    return sum(validate_score(scores[item]) for item in CHECKLIST_ITEMS)


def adjust_probability_from_score(
    baseline_probability: float,
    total_score: float,
    mean_score: float = 10.0,
    penalty_per_point: float = 0.05,
) -> float:
    """Adjust baseline probability using the deck's score logic.

    Lower scores are better. If a catalyst scores below the average score,
    the internal probability rises. If it scores above average, it falls.
    """

    scaled_score = float(total_score) - float(mean_score)
    adjustment = scaled_score * -float(penalty_per_point)
    return clip_probability(float(baseline_probability) + adjustment)


def score_to_probability(
    scores: Mapping[str, float],
    baseline_probability: float = 0.80,
    mean_score: float = 10.0,
    penalty_per_point: float = 0.05,
) -> float:
    """Convert a catalyst checklist into an internal probability estimate."""

    total_score = score_catalyst(scores)
    return adjust_probability_from_score(
        baseline_probability=baseline_probability,
        total_score=total_score,
        mean_score=mean_score,
        penalty_per_point=penalty_per_point,
    )

