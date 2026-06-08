PYTHON ?= python3

.PHONY: all test clean

all:
	PYTHONPATH=src $(PYTHON) -m c2o.cli run-all --config configs/default.yaml

test:
	PYTHONPATH=src:.test_deps $(PYTHON) -m pytest tests/

clean:
	rm -rf outputs/* report/generated_file_list.md
