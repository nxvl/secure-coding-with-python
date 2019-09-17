BRANCH := $(shell git rev-parse --abbrev-ref HEAD)
NEXT := $(shell python utils/brancher.py next $(BRANCH))
PREV := $(shell python utils/brancher.py prev $(BRANCH))

next:
	git checkout $(NEXT)

prev:
	git checkout $(PREV)

forward:
	git merge $(PREV)
