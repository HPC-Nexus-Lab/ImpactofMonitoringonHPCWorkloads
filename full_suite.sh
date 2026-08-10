#! /bin/bash

# Runs a test suite under the 5 differant conditions

set -xe

# Assumes we start with the base case
# clean up, just in case

ssh worker sudo systemctl stop hpcperfstats || :
ssh worker sudo systemctl reset-failed #stopping hpcperfstats always puts it into failed
ssh worker sudo systemctl stop ldms
sudo systemctl stop bmc-monitor
ssh worker sudo systemctl stop amsd.service smad.service cpqIde.service cpqScsi.service cpqFca.service cpqiScsi.service mr_cpqScsi.service

./reframe.sh "$@"  --session-extras test=no_monitoring

# start ith ldms
ssh worker sudo systemctl start ldms

sleep 10 # to settle
./reframe.sh "$@"  --session-extras test=ldms

# disable ldms, start BMC monitor and amsd on the node
ssh worker sudo systemctl stop ldms
ssh worker sudo systemctl start amsd
sudo systemctl start bmc-monitor

sleep 10 # to settle
./reframe.sh "$@"   --session-extras test=bmc_with_amsd_clean

# stop amsd and depends
sudo systemctl stop bmc-monitor
ssh worker sudo systemctl stop amsd.service smad.service cpqIde.service cpqScsi.service cpqFca.service cpqiScsi.service mr_cpqScsi.service

# Enable just the BMC monitor
sudo systemctl start bmc-monitor
sleep 10 # to settle
./reframe.sh "$@"   --session-extras test=bmc_no_amsd
sudo systemctl stop bmc-monitor

# Then turn on hpcperfstats
ssh worker sudo systemctl start hpcperfstats
sleep 10 # to settle
./reframe.sh "$@"  --session-extras test=hpcperfstats

#Disable it
ssh worker sudo systemctl stop hpcperfstats || :
ssh worker sudo systemctl reset-failed #stopping hpcperfstats always puts it into failed
