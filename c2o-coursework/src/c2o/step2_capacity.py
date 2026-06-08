"""Run Step 2 capacity-aware universe construction."""

from __future__ import annotations

from .notebook_pipeline import NotebookPipeline

CELL_IDS = [34, 35, 37, 39, 41, 43, 45, 47, 50, 54, 56, 58, 59, 61, 62, 64, 65, 66, 68]


def run_step2(pipeline: NotebookPipeline) -> None:
    """Run Step 2 capacity-aware universe construction."""

    pipeline.run_cells(CELL_IDS)
