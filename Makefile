.PHONY: build
build:
	docker build -t gpt-retrieval-api .

.PHONY: run
run:
	docker run -p 8000:8000 gpt-retrieval-api

.PHONY: all
all: build run