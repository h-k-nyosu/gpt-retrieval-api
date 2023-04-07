.PHONY: setup test run deploy export-requirements clean

default: run

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
	poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

deploy: export-requirements
	@echo "Deploying the app"
	vercel .

export-requirements:
	@echo "Exporting requirements.txt"
	poetry export -f requirements.txt -o requirements.txt --without-hashes
	@echo "Exported requirements.txt"

clean:
	@echo "Cleaning environment"
	find . -type d -name __pycache__ -exec rm -r {} +
	rm -rf .pytest_cache
	@echo "Cleanup complete"