#!/usr/bin/env bash

DIR=$(pwd)

pytest -x -vv -s $DIR/tests/
pytest -x -vv -s $DIR/bot/tests/

pytest_exit_code=$?
echo $pytest_exit_code

exit $pytest_exit_code
