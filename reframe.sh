#! /bin/bash

# Wraps reframe so that it's path-independant (hopefully)

cd $(dirname $0)

RFM_PREFIX=reframe/.results/ reframe -C reframe/settings.py -c reframe/tests/ "$@"