from __future__ import annotations

import numpy as np


def test_return_reconciliation(panel):
    valid = panel[["r_on", "r_id", "r_cc"]].replace([np.inf, -np.inf], np.nan).dropna()
    residual = ((1 + valid["r_on"]) * (1 + valid["r_id"]) - 1 - valid["r_cc"]).abs().max()
    assert residual < 1e-8


def test_clean_panel_has_no_duplicate_stock_days(panel):
    assert not panel.duplicated(["date", "instrument_id"]).any()
