POETRY_VERSION :=$(shell poetry --version)

poetry/setup:
ifdef POETRY_VERSION
	@echo "Found poetry version $(POETRY_VERSION)"
else
	@echo "Poetry not found, starting to install poetry"
	pip install pip -U
	pip install setuptools
	pip install poetry
	@echo "Installed poetry version" $(shell poetry --version)
endif

poetry/install-dependencies:
	poetry install

code-quality/setup:
	poetry add flake8
	poetry add unimport
	poetry add isort
	poetry add black
	poetry add pytest

code-quality/format:
	poetry run unimport -r .
	poetry run isort .
	poetry run black .

code-quality/scan: code-quality/format
	poetry run flake8
	poetry run unimport --check .
	poetry run isort --check .
	poetry run black --check .

code-quality/tests:
	poetry run pytest tests/

run/infra/start:
	docker-compose up -d database cache
	sleep 5

run/infra/stop:
	docker-compose down

run/infra/database/migrate: run/infra/start
	poetry run python app/manage.py migrate

run/api/createsuperuser: run/infra/database/migrate
	poetry run python app/manage.py createsuperuser

run/api/start: run/infra/start
	docker-compose up -d api
