#!/usr/bin/env bash
source myapp/bin/activate
python __init__.py > /dev/null &
nosetests --with-coverage