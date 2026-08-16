This directory and subdirectories contain the reFrame tests necessary to 
reproduce the experiments. There is some setup required in terms of providing 
code (and configuring HPL).

# NPB

The [NASA Parallel Benchmark](https://www.nas.nasa.gov/software/npb.html) suite 
should be downloaded and untarred. The resulting directory should be copied to 
the `reframe` directory under the name `npb`.

# HPL

[Download HPL](https://www.netlib.org/benchmark/hpl/) and untar it. Copy the 
resulting directory to `reframe/` and name it `hpl`.

HPL's configuration is unfortunately location dependent. To run under reFrame,
it must be location independent. We provide `Make.Linux_intel64` as an example
of a location-independent configuration. Specifically, the `TOPdir` variable
is adjusted to be location-independent. This version is configured for 
openmpi/openblas.

For an exact reproduction, you will also have to copy the HPL config file from 
`benchmark_configs/` into the `hpl/` directory.