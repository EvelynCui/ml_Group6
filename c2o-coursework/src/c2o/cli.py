"""Command line interface for reproducing the coursework artifacts."""

from __future__ import annotations

import argparse
from pathlib import Path

from .config import load_config
from .notebook_pipeline import NotebookPipeline
from .reporting import finalise_reporting, write_generated_file_list
from .step1_panel import run_step1
from .step2_capacity import run_step2
from .step3_borrow import run_step3
from .step4_alpha import run_step4
from .step5_backtest import run_step5


def run_all(config_path: str | Path) -> dict[str, str]:
    """Run every reproduction step from raw inputs to final reports."""

    config = load_config(config_path)
    pipeline = NotebookPipeline(config)
    run_step1(pipeline)
    run_step2(pipeline)
    run_step3(pipeline)
    run_step4(pipeline)
    run_step5(pipeline)
    manifest = finalise_reporting(pipeline)
    write_generated_file_list(config.project_root, manifest)
    return manifest


def main(argv: list[str] | None = None) -> None:
    """Parse CLI arguments and dispatch commands."""

    parser = argparse.ArgumentParser(description="Reproduce C2O coursework outputs.")
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run-all", help="Run the full reproduction pipeline.")
    run.add_argument("--config", default="configs/default.yaml", help="Path to the YAML configuration file.")
    args = parser.parse_args(argv)
    if args.command == "run-all":
        run_all(args.config)


if __name__ == "__main__":
    main()
