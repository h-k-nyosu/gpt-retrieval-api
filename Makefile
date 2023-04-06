.PHONY: setup test run build all export-requirements install-requirements clean

# Set the name of the Docker image to be built
IMAGE_NAME=gpt-retrieval-api

setup:
	@echo "Setting up environment"
	poetry install
	@echo "Setup complete"

test:
	@echo "Running tests"
	poetry run pytest tests/
	@echo "Tests complete"

run:
	@echo "Running the app"
	docker run -p 8000:8000 $(IMAGE_NAME)

build:
	@echo "Exporting requirements.txt"
	poetry export -f requirements.txt -o requirements.txt --without-hashes
	@echo "Exported requirements.txt"

	@echo "Building Docker image"
	docker build -t $(IMAGE_NAME) .
	@echo "Docker image built"

all: build run

install-requirements:
	@echo "Installing requirements"
	pip install -r requirements.txt
	@echo "Installed requirements"

clean:
	@echo "Cleaning environment"
	find . -type d -name __pycache__ -exec rm -r {} +
	rm -rf .pytest_cache
	@echo "Cleanup complete"