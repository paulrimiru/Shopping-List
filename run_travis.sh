#!/usr/bin/env bash
python myapp/__init__.py > /dev/null &
nosetests --with-coverage