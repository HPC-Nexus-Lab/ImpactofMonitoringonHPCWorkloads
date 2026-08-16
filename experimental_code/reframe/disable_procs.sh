#! /bin/bash

set -xe

COUNT=$( ls /sys/devices/system/cpu/cpufreq/ | wc -l )

echo "Using ${1} of ${COUNT}, take ${COUNT}-${1} offline"

PROCS=$(
    python3 -c "from numpy import linspace
for val in linspace(1, ${COUNT}-1, ${COUNT}-${1}):
    print(f\"/sys/devices/system/cpu/cpu{int(val)}/online\")
"
)

for FILE in $PROCS
do
    echo 0 | sudo tee $FILE
done