from __future__ import annotations

from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def test_portfolio_consistency(daily_returns):
    assert "net_return" in daily_returns.columns
    assert np.isfinite(daily_returns["net_return"].dropna()).all()
    if {"gross_return", "total_cost_return"}.issubset(daily_returns.columns):
        diff = (daily_returns["gross_return"] - daily_returns["total_cost_return"] - daily_returns["net_return"]).abs().max()
        assert diff < 1e-8


def test_quantstats_headline_path_and_inputs(daily_returns):
    assert (ROOT / "outputs" / "tear_sheets" / "quantstats_250m_sp500_tr.html").exists()
    assert "net_return" in daily_returns.columns
    assert daily_returns["net_return"].notna().any()
    text = (ROOT / "outputs" / "manifest.json").read_text()
    assert "quantstats_250m_sp500_tr.html" in text
