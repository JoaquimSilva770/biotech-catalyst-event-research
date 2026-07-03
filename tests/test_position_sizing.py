import pytest

from biotech_catalyst.position_sizing import (
    edge_scaled_weight,
    expected_return_from_scenarios,
    kelly_fraction_binary,
)


def test_expected_return_from_scenarios() -> None:
    expected_return = expected_return_from_scenarios(
        current_price=100,
        approval_price=130,
        failure_price=80,
        model_probability=0.70,
    )

    assert expected_return == pytest.approx(0.15)


def test_edge_scaled_weight_is_zero_inside_neutral_band() -> None:
    assert edge_scaled_weight(0.62, 0.60, neutral_band=0.05) == pytest.approx(0.0)


def test_edge_scaled_weight_is_capped() -> None:
    assert edge_scaled_weight(1.0, 0.0, neutral_band=0.0, max_weight=0.10) == pytest.approx(0.10)


def test_kelly_fraction_binary_positive_for_good_edge() -> None:
    fraction = kelly_fraction_binary(0.70, 0.30, -0.15)

    assert fraction > 0
