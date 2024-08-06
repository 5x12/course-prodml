.PHONY: run_builder run_inference install clean check runner_builder runner_inference
.DEFAULT_GOAL:=runner_inference

run_builder: install
	cd src; poetry run python3 runner_builder.py 

run_inference: install
	cd src; poetry run python3 runner_inference.py 

install: pyproject.toml
	poetry install

clean:
	rm -rf `find . -type d -name __pycache__`

check:
	poetry run flake8 src/

runner_builder: check run_builder clean

runner_inference: check run_inference clean