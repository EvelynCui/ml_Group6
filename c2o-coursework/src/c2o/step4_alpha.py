"""Run Step 4 alpha signal construction."""

from __future__ import annotations

from .notebook_pipeline import NotebookPipeline

CELL_IDS = [99, 100, 102]


def run_step4(pipeline: NotebookPipeline) -> None:
    """Run Step 4 alpha signal construction."""

    pipeline.run_cells(CELL_IDS)
