"""Input and output helpers for generated artifacts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Mapping


def ensure_output_layout(output_dir: Path) -> None:
    """Create the standard output directory tree."""

    for child in ["intermediate", "tables", "figures", "tear_sheets"]:
        (output_dir / child).mkdir(parents=True, exist_ok=True)


def write_manifest(output_dir: Path, entries: Mapping[str, str]) -> Path:
    """Write the JSON manifest for generated files."""

    path = output_dir / "manifest.json"
    path.write_text(json.dumps(dict(entries), indent=2, sort_keys=True) + "\n")
    return path
