"""Run Step 5 portfolio construction and backtest."""

from __future__ import annotations

from .notebook_pipeline import NotebookPipeline

CELL_IDS = [104, 105, 107, 109, 111]


def run_step5(pipeline: NotebookPipeline) -> None:
    """Run Step 5 portfolio construction and backtest."""

    pipeline.run_cells(CELL_IDS)
