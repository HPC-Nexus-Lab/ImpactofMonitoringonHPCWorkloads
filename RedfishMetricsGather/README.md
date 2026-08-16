This directory contains the script to gather metrics from the BMC over Redfish.

# Installation

Copy this directory to a location on the node which will be performing the 
monitoring.

1. Change to that directory
2. Create a python virtualenv:
   ```shell
   python3 -m venv .venv
   ```
3. Enter the venv and install the required packages:
   ```shell
   source .venv/bin/activate
   pip install -r requirements.txt
   ```