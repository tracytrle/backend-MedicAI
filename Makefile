# Makefile for Python Flask application

# Variables
APP_NAME = medicai
APP_ENV  = development
VENV_DIR = venv
CURRENT_DIR=$(shell pwd)

# Commands
.PHONY: help setup install run clean dbmigrate dbinit shell freeze

help:
	@echo "Makefile commands:"
	@echo "  setup   - Create virtual environment and install dependencies"
	@echo "  install - Install dependencies"
	@echo "  run     - Run the Flask application"
	@echo "  clean   - Remove virtual environment"
	@echo "  dbupgrade - Run the Flask upgrade"
	@echo "  dbinit  - Run the Flask migration"
	@echo "  shell   - Run the Flask shell"
	@echo "  freeze  - Freeze the dependencies"
	@echo "  dbmigrate - Run the Flask migration with message"

setup: $(VENV_DIR)

$(VENV_DIR):
	@echo "Creating virtual environment..."
	python3 -m venv $(VENV_DIR)
	@echo "Installing dependencies..."
	$(VENV_DIR)/bin/pip install -r requirements.txt

install:
	@echo "Installing dependencies..."
	$(VENV_DIR)/bin/pip install -r requirements.txt

run:
	@echo "Running the Flask application..."
	PYTHONPATH=$(CURRENT_DIR)/$(APP_NAME) FLASK_APP=$(APP_NAME) FLASK_ENV=$(APP_ENV) $(VENV_DIR)/bin/flask run --host=0.0.0.0 --port=5005

clean:
	@echo "Removing virtual environment..."
	rm -rf $(VENV_DIR)


dbmigrate: 
# example run: make dbmigrate m="create user table"
	@echo "Running the Flask migration with message: $(m)"
	PYTHONPATH=$(CURRENT_DIR)/$(APP_NAME) FLASK_APP=$(APP_NAME) FLASK_ENV=$(APP_ENV) $(VENV_DIR)/bin/flask db migrate  -m "$(m)"

dbupgrade:
	@echo "Running the Flask migration..."
	PYTHONPATH=$(CURRENT_DIR)/$(APP_NAME) FLASK_APP=$(APP_NAME) FLASK_ENV=$(APP_ENV) $(VENV_DIR)/bin/flask db upgrade

dbinit:
	@echo "Running the Flask migration..."
	echo "$(CURRENT_DIR)/$(APP_NAME)"
	echo "$(APP_NAME)"
	PYTHONPATH=$(CURRENT_DIR)/$(APP_NAME) FLASK_APP=$(APP_NAME) FLASK_ENV=$(APP_ENV) $(VENV_DIR)/bin/flask db init

shell:
	@echo "Running the Flask shell..."
	PYTHONPATH=$(CURRENT_DIR)/$(APP_NAME) FLASK_APP=$(APP_NAME) FLASK_ENV=$(APP_ENV) $(VENV_DIR)/bin/flask shell

freeze:
	pip freeze > requirements.txt