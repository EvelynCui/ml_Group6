# C2O Coursework Reproduction Repository

## Project Overview

This repository reproduces the close-to-open equity strategy outputs used in the coursework report and QuantStats tear-sheet. The implementation follows the submitted notebook logic while packaging the workflow as a reproducible Python project with a stable command line entry point, configuration file, tests, and generated artifact manifest.

## Brief Compliance Statement

The pipeline starts from raw input files, rebuilds the point-in-time daily panel, capacity-aware universe, borrow-cost table, alpha scores, portfolio returns, figures, report tables, and the 250m AUM QuantStats tear-sheet benchmarked to `SP500_TR`.

## Environment Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Required Raw Data

Place these files in `data/`:

- `prices.parquet`
- `earnings_calendar.parquet`
- `short_interest_transfo.parquet`
- `sp500_tr.parquet`

## Full Reproduction

```bash
make all
```

Equivalent command:

```bash
PYTHONPATH=src python -m c2o.cli run-all --config configs/default.yaml
```

## Tests

```bash
make test
```

## Output Structure

- `outputs/`: step outputs, generated tables, and compatibility artifacts.
- `outputs/figures/`: all report figures.
- `outputs/tear_sheets/quantstats_250m_sp500_tr.html`: headline QuantStats tear-sheet.
- `outputs/manifest.json`: stable manifest of generated files.
- `report/generated_file_list.md`: report-facing artifact list.

## Reproducibility Notes

The random seed is fixed at `42`. The yearly universe is frozen using the final trading day of the previous calendar year. Earnings events are shifted to the first tradable overnight window after public availability. Short-interest data uses the source-provided availability lag and the daily merge applies the previous-trading-day as-of rule. Capacity constraints apply the participation cap before portfolio weights are normalised.

## Known Limitations

The repository assumes the raw parquet files match the coursework data schema. Strategy selection, parameters, and headline reporting are intentionally kept aligned with the audited notebook logic rather than re-optimised.
