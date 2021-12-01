# makefile

install:
	python3 -m poetry install

publish:
	python3 -m poetry publish --dry-run
	
lint:
	python3 -m poetry run flake8

test:
	python3 -m poetry run python manage.py test

test-coverage:
	poetry run pytest --cov=page_loader --cov-report xml

test-run:
	python3 -m poetry run python manage.py runserver

migration:
	python3 -m poetry run python manage.py makemigrations
	python3 -m poetry run python manage.py migrate

heroku-run:
	poetry run heroku local

req-export:
	poetry export -f requirements.txt --output requirements.txt

heroku-log:
	poetry run heroku logs --tail --app angekoks-task-manager

translate:
	python3 -m poetry run python manage.py makemessages --locale=ru

compil-translate:
	python3 -m poetry run django-admin compilemessages