from __future__ import annotations


def test_capacity_cap_not_exceeded(positions):
    required = {"abs_position_notional", "adv_cap_notional"}
    assert required.issubset(positions.columns)
    rows = positions.dropna(subset=["abs_position_notional", "adv_cap_notional"])
    assert (rows["abs_position_notional"] <= rows["adv_cap_notional"] + 1e-6).all()


def test_no_forced_gross_overdeployment(daily_returns):
    assert "deployed_gross_ratio" in daily_returns.columns
    assert (daily_returns["deployed_gross_ratio"].dropna() <= 1.0000001).all()
