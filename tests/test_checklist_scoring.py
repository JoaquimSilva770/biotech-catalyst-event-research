import pytest

from biotech_catalyst.checklist_scoring import adjust_probability_from_score, score_catalyst


def test_score_catalyst_sums_required_items() -> None:
    score = score_catalyst(
        {
            "endpoint_strength": 1,
            "safety": 2,
            "regulatory_classification": 1,
            "cmc_risk": 2,
            "standard_of_care": 1,
        }
    )

    assert score == pytest.approx(7)


def test_adjust_probability_rewards_better_than_average_score() -> None:
    probability = adjust_probability_from_score(
        baseline_probability=0.80,
        total_score=8,
        mean_score=10,
        penalty_per_point=0.05,
    )

    assert probability == pytest.approx(0.90)


def test_score_catalyst_rejects_out_of_range_score() -> None:
    with pytest.raises(ValueError):
        score_catalyst(
            {
                "endpoint_strength": 5,
                "safety": 2,
                "regulatory_classification": 1,
                "cmc_risk": 2,
                "standard_of_care": 1,
            }
        )

