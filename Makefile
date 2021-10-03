.DEFAULT_GOAL := check

venv:
	python -m venv venv
	. venv/bin/activate
	@which python
	@python -V

update: venv
	python -m pip install -U pip
	pip install -U -r requirements.txt

check: venv
	flake8 src
	black --diff src

format: venv
	black src
