# BRMFlask [![Build Status](https://travis-ci.org/brmullikin/BRMFlask.svg?branch=master)](https://travis-ci.org/brmullikin/BRMFlask) [![Coverage Status](https://coveralls.io/repos/github/brmullikin/BRMFlask/badge.svg)](https://coveralls.io/github/brmullikin/BRMFlask)

A better readme.md coming soon...

## Setup

To set up, run ```pip install --editable```

## test

Run tests with: ```py.test -v brmflask```


### See Test Coverage

Run coverage with: ```py.test -v --cov-report term-missing --cov brmflask```

### Flake8

See Flake8 compatibility with: ```Flake8 --max-line-length=100 --ignore=E302,D203 --exclude __init__.py brmflask```

**note:** I ignore E302 & D203 in favor of PEP257 rules, especially D211 and extend the max-line to 100 (Because [Beyond Pep8](https://www.youtube.com/watch?v=wf-BqAjZb8M) & [A Foolish Consistency is the Hobgoblin of Little Minds](https://www.python.org/dev/peps/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds)).

