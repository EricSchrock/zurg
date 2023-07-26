.PHONY: all
all: test run

.PHONY: run
run:
	python3 zurg.py

.PHONY: test
test:
	pytest -v

.PHONY: docs
docs:
	pydoc-markdown -m zurg -I . > docs/ZURG.md
