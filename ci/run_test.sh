#!/usr/bin/env bash

DIR=$(pwd)

# 子文件夹在先，根目录在最后，否则生成的 coverage.xml 有问题
pytest -x -vv -s --cov=./bot --cov-report=xml:coverage-reports/coverage.xml $DIR/bot/tests/ \
    && pytest -x -vv -s --cov=./ --cov-append --cov-report=xml:coverage-reports/coverage.xml $DIR/tests/

#pytest_exit_code=$?
#echo $pytest_exit_code

#exit $pytest_exit_code
