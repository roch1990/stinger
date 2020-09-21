.PHONY: tests
tests:
	docker build -f Dockerfile.test .

.PHONY: help
help:
	@echo "You can run this helpful commands:"
	@echo
	@echo -e "\tmake tests       start tests"
