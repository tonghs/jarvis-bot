#!/usr/bin/env bash

DIR=$(pwd)

pytest -x -vv -s --cov=./bot --cov-report=xml:coverage-reports/coverage.xml $DIR/bot/tests/ \
    && pytest -x -vv -s --cov=./ --cov-append --cov-report=xml:coverage-reports/coverage.xml $DIR/tests/

#pytest_exit_code=$?
#echo $pytest_exit_code

#exit $pytest_exit_code
