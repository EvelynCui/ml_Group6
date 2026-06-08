from __future__ import annotations

import pandas as pd


def test_earnings_effective_dates_are_available(panel):
    cols = {"effective_date", "reporting_date"}
    if cols.issubset(panel.columns):
        rows = panel.dropna(subset=["effective_date", "reporting_date"])
        assert (pd.to_datetime(rows["effective_date"]) >= pd.to_datetime(rows["reporting_date"])).all()


def test_short_interest_previous_day_asof(step3):
    rows = step3.dropna(subset=["si_publication_available_trading_date"])
    assert (pd.to_datetime(rows["si_publication_available_trading_date"]) < pd.to_datetime(rows["date"])).all()


def test_alpha_rows_have_next_overnight_target(panel):
    rows = panel.loc[panel["eligible"]]
    assert rows["target_next_overnight"].notna().any()
    assert rows["expected_next_trading_day"].notna().any()
