from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"


@pytest.fixture(scope="session")
def panel() -> pd.DataFrame:
    return pd.read_parquet(OUT / "c2o_step1_clean_panel.parquet")


@pytest.fixture(scope="session")
def step2() -> pd.DataFrame:
    return pd.read_parquet(OUT / "c2o_step2_prelim_tradable_universe.parquet")


@pytest.fixture(scope="session")
def step3() -> pd.DataFrame:
    return pd.read_parquet(OUT / "c2o_step3_borrow_tiers.parquet")


@pytest.fixture(scope="session")
def positions() -> pd.DataFrame:
    return pd.read_parquet(OUT / "step5_positions.parquet")


@pytest.fixture(scope="session")
def daily_returns() -> pd.DataFrame:
    return pd.read_csv(OUT / "step5_headline_daily_returns.csv", parse_dates=["date"])
