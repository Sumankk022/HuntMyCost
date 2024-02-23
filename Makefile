# Makefile

# Define the default target
all: setup test run

# Target to install dependencies
setup:
	poetry install

# Target to run tests
test:
	poetry run pytest

# Target to run the FastAPI app
run:
	poetry run uvicorn main:app --reload
