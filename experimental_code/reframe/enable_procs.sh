#! /bin/bash

set -xe

for FILE in $( ls /sys/devices/system/cpu/cpu*/online )
do
    echo 1 | sudo tee $FILE
done