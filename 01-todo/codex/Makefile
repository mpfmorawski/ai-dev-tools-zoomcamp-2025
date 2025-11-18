UV=uv
MANAGE=$(UV) run python todo_project/manage.py

.PHONY: help install runserver migrations migrate superuser check shell test

help:
	@echo "Common targets:"
	@echo "  make install      Install dependencies via uv"
	@echo "  make runserver    Start Django dev server"
	@echo "  make migrations   Create migrations for changes"
	@echo "  make migrate      Apply database migrations"
	@echo "  make superuser    Create an admin user"
	@echo "  make check        Run Django system checks"
	@echo "  make shell        Open Django shell"
	@echo "  make test         Run Django test suite"

install:
	$(UV) sync

runserver:
	$(MANAGE) runserver 0.0.0.0:8000

migrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

superuser:
	$(MANAGE) createsuperuser

check:
	$(MANAGE) check

shell:
	$(MANAGE) shell

test:
	$(MANAGE) test
