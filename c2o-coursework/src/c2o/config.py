"""Configuration loading for the reproduction pipeline."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import yaml
except Exception:  # pragma: no cover
    yaml = None


@dataclass(frozen=True)
class PipelineConfig:
    """Resolved configuration values used by all pipeline steps."""

    project_root: Path
    raw_data_dir: Path
    output_dir: Path
    values: dict[str, Any]


def _parse_scalar(value: str) -> Any:
    value = value.strip()
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    if value in {"true", "false"}:
        return value == "true"
    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        return value


def _minimal_yaml(text: str) -> dict[str, Any]:
    data: dict[str, Any] = {}
    current: str | None = None
    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if not raw_line.startswith(" ") and ":" in raw_line:
            key, value = raw_line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value == "":
                data[key] = {}
                current = key
            elif value.startswith("[") and value.endswith("]"):
                data[key] = [_parse_scalar(v.strip()) for v in value[1:-1].split(",") if v.strip()]
                current = None
            else:
                data[key] = _parse_scalar(value)
                current = None
        elif current and ":" in raw_line:
            key, value = raw_line.strip().split(":", 1)
            data[current][key.strip()] = _parse_scalar(value.strip())
    return data


def load_config(config_path: str | Path) -> PipelineConfig:
    """Load and resolve a YAML configuration file."""

    path = Path(config_path).resolve()
    text = path.read_text()
    values = yaml.safe_load(text) if yaml is not None else _minimal_yaml(text)
    project_root = path.parent.parent
    raw_data_dir = (project_root / values.get("raw_data_dir", "data")).resolve()
    output_dir = (project_root / values.get("output_dir", "outputs")).resolve()
    return PipelineConfig(project_root=project_root, raw_data_dir=raw_data_dir, output_dir=output_dir, values=values)
