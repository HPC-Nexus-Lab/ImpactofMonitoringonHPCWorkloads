#! /bin/bash

# Wraps reframe so that it's path-independant (hopefully)

cd $(dirname $0)

reframe "$@"