import pytest

from biotech_catalyst.implied_probability import (
    breakeven_probability,
    market_implied_probability,
    scenario_prices,
)


def test_market_implied_probability_from_cytokinetics_case() -> None:
    implied = market_implied_probability(
        current_price=60.32,
        approval_price=71.19,
        failure_price=43.77,
    )

    assert implied == pytest.approx(0.6036, abs=1e-4)


def test_breakeven_probability() -> None:
    probability = breakeven_probability(0.177, -0.137)

    assert probability == pytest.approx(0.4363, abs=1e-4)


def test_scenario_prices() -> None:
    approval_price, failure_price = scenario_prices(100, 0.20, -0.10)

    assert approval_price == pytest.approx(120)
    assert failure_price == pytest.approx(90)


def test_market_implied_probability_rejects_flat_scenarios() -> None:
    with pytest.raises(ValueError):
        market_implied_probability(100, 90, 90)

