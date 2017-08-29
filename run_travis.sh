#!/usr/bin/env bash
python __init__.py > /dev/null &
nosetests --with-coverage