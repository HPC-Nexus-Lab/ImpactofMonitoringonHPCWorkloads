This directory contains the configuration files for monitoring, as well as the 
code for the custom BMC monitor script.

# LDMS

LDMS has two configuration files in this directory:

- `ldms_agg.conf`, for the LDMS aggregator, which is installed on the admin node
- `sampler.conf`, which is installed on the copute node(s)

All files go in `/etc/ldms` on their respective nodes

# HPCPerfStats

HPCPerfStats has just one file, `hpcperfstats.conf`. This is installed in
`/etc/hpcperfstats`. You may need to adjust the `server` line to point to your
rabbitmq installation.

# BMC monitor

The BMC monitor has three files in this directory:

- `bmc-monitor` - the launch script. Install in `/usr/local/bin` and adjust
  the paths to the virtualenv `python3` executable, `gather.py`, and 
  `urls-worker` file to match your setup. Also adjust `metricsuser` and
  `metricspass` to be the correct username and password for your BMC.
- `bmc-monitor.service` - a systemd service for the script. Copy to 
  `/etc/systemd/system/bmc-monitor.service`

Don't forget to install the script as documented in the `RedfishMetricsGather/`
directory.