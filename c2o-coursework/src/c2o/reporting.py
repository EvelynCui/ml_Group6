"""Reporting helpers for the final artifact manifest."""

from __future__ import annotations

from pathlib import Path

from .notebook_pipeline import NotebookPipeline


def finalise_reporting(pipeline: NotebookPipeline) -> dict[str, str]:
    """Create stable reporting paths and the JSON manifest."""

    return pipeline.finalise_outputs()


def write_generated_file_list(project_root: Path, manifest: dict[str, str]) -> Path:
    """Write a report-facing list of generated files."""

    report_dir = project_root / "report"
    report_dir.mkdir(parents=True, exist_ok=True)
    path = report_dir / "generated_file_list.md"
    rows = ["# Generated File List", ""]
    for key, value in sorted(manifest.items()):
        rows.append(f"- `{key}`: `{value}`")
    path.write_text("\n".join(rows) + "\n")
    return path
