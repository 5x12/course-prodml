.PHONY: run install clean check runner
.DEFAULT_GOAL:=runner

run: install
	cd app; poetry run python3 run.py 

install: pyproject.toml
	poetry install

clean:
	rm -rf `find . -type d -name __pycache__`

check:
	poetry run flake8 app/

runner: check run clean
