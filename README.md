This repository contains the artifacts from the paper "Measuring the Impact of 
Monitoring on HPC Workloads". The histogram figures mentioned in the paper can
be found in [Paper/appendix_figures](Paper/appendix_figures/README.md).

It is structured as follows:

- `analysis_code` - The Jupyter notebook used to perform analysis on the results
- `banchmark_configs` - Configuration files for specific benchmarks
- `experimental_code` - Code for the benchmarks and running of the benchmarks
- `monitoring` - Configuration for the various monitoring systems
- `os_artifacts` - Artifacts describing the OS and runtime of the test environment
- `Paper` - Source files for the written paper
- `RedfishMetricsGather` - scripts to gather metrics from the BMC via Redfsih
- `results` - the reFrame results directory used to calculate numbers in the paper
- `rpmbuild` - Configuration files to build custom RPMs for monitoring systems
- `wlm` - SLURM configuration file(s)


# Setup

In order to set up a full reproduction enviornment:

1. Choose a directory and create a python virtual environment there. (
    `python3 -m venv .venv`, for example)
2. Copy the `experimental_code/reframe/` directory into that directory
3. Copy `PilotStudy.ipynb` and `StatsTests.ipynb` into that directory.
4. Copy `requirements.txt` into that directory
4. Activate the virtualenv and install the requirements:
    ```
    source .venv/bin/activate
    pip install -r requirements.txt
    ```
6. Follow the directions in `experimental_code/README.md` to set up the tests
7. Install and configure LDMS, HPCPerfStats, and the BMC monitoring script 
    using the directions in `rpmbuild/` and `monitoring/`.
8. Instal [`amsd`](https://support.hpe.com/connect/s/softwaredetails?language=en_US&collectionId=MTX-c8581e07bdde4d55&tab=releaseNotes) on the machine
9. Follow the install directions in `RedfishMetricsGather/` to install the BMC
   monitoring script.

# Running tests

The pilot tests can be run as:

```shell
for I in {1..4}; do ./full_suite.sh -n hpl_test --run --session-extras benchmark=hpl --repeat=5; done
for I in {1..4}; do ./full_suite.sh -n sp_test -S problem_size=C -S r_num_tasks=49 --run --session-extras benchmark=sp --session-extras problem_size=C --session-extras tasks=49 --repeat=5; done
for I in {1..4}; do ./full_suite.sh -n ep_test -S problem_size=E --run --session-extras benchmark=ep --session-extras jobsize=E --repeat=5; done ;
for I in {1..4}; do ./full_suite.sh -n ep_test -S problem_size=D --run --session-extras benchmark=ep --session-extras jobsize=D --repeat=5; done ;
```

This will run HPL, then SP, then EP size E and finally EP size D, 20 
repetitions each.

The pilot tests should then be examined using the `PilotTest.ipynb` Jupyter
notebook to determine the correct number of tests needed for full results.
The same commands can be used to run the full tests, however the number of 
repetitions (the `4` in `{1..4}`) will need to be adjusted to the number of 
repetitions divided by 5.