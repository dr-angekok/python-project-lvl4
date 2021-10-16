# makefile

install:
	python3 -m poetry install

publish:
	python3 -m poetry publish --dry-run
	
lint:
	python3 -m poetry run flake8

test:
	python3 -m poetry run pytest

extended-test:
	python3 -m poetry run pytest -vv

test-coverage:
	poetry run pytest --cov=page_loader --cov-report xml

test-run:
	poetry run python manage.py runserver

heroku-run:
	poetry run heroku local

req-export:
	poetry export -f requirements.txt --output requirements.txt

heroku-log:
	poetry run heroku logs --tail --app angekoks-task-manager