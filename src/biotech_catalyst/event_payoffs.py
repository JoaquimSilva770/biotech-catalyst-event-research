"""Event-study helpers for PDUFA/FDA catalyst returns."""

from __future__ import annotations

import pandas as pd

from biotech_catalyst.implied_probability import breakeven_probability


def normalise_outcome(value: str) -> str:
    """Map outcome labels into APPROVED or CRL."""

    text = str(value).strip().upper()
    if text in {"APPROVED", "APPROVAL", "APPROVE"}:
        return "APPROVED"
    if text in {"CRL", "COMPLETE RESPONSE LETTER", "REJECTED"}:
        return "CRL"
    return text


def compute_abnormal_return(stock_return: float, benchmark_return: float) -> float:
    """Stock return minus benchmark return over the same event window."""

    return float(stock_return) - float(benchmark_return)


def summarise_event_payoffs(
    events: pd.DataFrame,
    return_col: str = "abnormal_return_5d",
    outcome_col: str = "outcome",
) -> dict[str, float]:
    """Summarise approval and CRL payoffs from an event-level table."""

    frame = events.copy()
    frame[outcome_col] = frame[outcome_col].map(normalise_outcome)
    approved = frame.loc[frame[outcome_col] == "APPROVED", return_col].dropna()
    crl = frame.loc[frame[outcome_col] == "CRL", return_col].dropna()

    if approved.empty or crl.empty:
        raise ValueError("both APPROVED and CRL observations are required")

    approval_mean = float(approved.mean())
    crl_mean = float(crl.mean())
    approval_median = float(approved.median())
    crl_median = float(crl.median())

    return {
        "sample_size": float(len(frame)),
        "approval_count": float((frame[outcome_col] == "APPROVED").sum()),
        "crl_count": float((frame[outcome_col] == "CRL").sum()),
        "approval_rate": float((frame[outcome_col] == "APPROVED").mean()),
        "approval_mean": approval_mean,
        "crl_mean": crl_mean,
        "approval_median": approval_median,
        "crl_median": crl_median,
        "breakeven_probability_mean": breakeven_probability(approval_mean, crl_mean),
        "breakeven_probability_median": breakeven_probability(approval_median, crl_median),
    }


def payoff_distribution(
    events: pd.DataFrame,
    return_col: str = "abnormal_return_5d",
    outcome_col: str = "outcome",
) -> pd.DataFrame:
    """Return a tidy approval-vs-CRL payoff table."""

    frame = events[[outcome_col, return_col]].copy()
    frame[outcome_col] = frame[outcome_col].map(normalise_outcome)
    return frame.dropna().rename(columns={outcome_col: "outcome", return_col: "abnormal_return"})

