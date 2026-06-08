from __future__ import annotations

import pandas as pd

from conftest import OUT


def test_universe_uses_prior_year_snapshot(panel):
    eligible = panel.loc[panel["eligible"]].copy()
    rows = eligible[["year", "universe_asof_date"]].drop_duplicates()
    assert not rows.empty
    assert (pd.to_datetime(rows["universe_asof_date"]).dt.year == rows["year"] - 1).all()


def test_universe_has_twelve_month_history(panel):
    audit = pd.read_csv(OUT / "c2o_step1_universe_sanity_by_year.csv")
    assert (audit["min_months_hist"] >= 12).all()
