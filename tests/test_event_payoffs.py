import pandas as pd
import pytest

from biotech_catalyst.event_payoffs import compute_abnormal_return, summarise_event_payoffs


def test_compute_abnormal_return() -> None:
    assert compute_abnormal_return(0.12, 0.02) == pytest.approx(0.10)


def test_summarise_event_payoffs() -> None:
    events = pd.DataFrame(
        {
            "outcome": ["APPROVED", "APPROVED", "CRL"],
            "abnormal_return_5d": [0.10, 0.30, -0.20],
        }
    )

    summary = summarise_event_payoffs(events)

    assert summary["approval_count"] == pytest.approx(2)
    assert summary["crl_count"] == pytest.approx(1)
    assert summary["approval_rate"] == pytest.approx(2 / 3)
    assert summary["approval_mean"] == pytest.approx(0.20)
    assert summary["crl_mean"] == pytest.approx(-0.20)
    assert summary["breakeven_probability_mean"] == pytest.approx(0.50)

