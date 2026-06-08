"""Run Step 3 borrow-cost and short-leg eligibility construction."""

from __future__ import annotations

from .notebook_pipeline import NotebookPipeline

CELL_IDS = [71, 72, 74, 75, 77, 79, 81, 83, 85, 87, 88, 90, 92, 93, 95, 96, 97]


def run_step3(pipeline: NotebookPipeline) -> None:
    """Run Step 3 borrow-cost and short-leg eligibility construction."""

    pipeline.run_cells(CELL_IDS)
