"""Run Step 1 point-in-time data panel construction."""

from __future__ import annotations

from .notebook_pipeline import NotebookPipeline

CELL_IDS = [2, 4, 6, 8, 10, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 30]


def run_step1(pipeline: NotebookPipeline) -> None:
    """Run Step 1 point-in-time data panel construction."""

    pipeline.run_cells(CELL_IDS)
