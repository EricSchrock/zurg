.PHONY: all
all: test run

.PHONY: run
run:
	python3 zurg.py

.PHONY: test
test:
	pytest -v
