This directory contians the files to build RPMs of LDMS and HPCPerfStats.
Both builds are somewhat custom and not guranteed to be configurable. They are 
as used in the paper, and should not be assumed correct for all use cases.

# LDMS

In order to build LDMS, run `build_ldms.sh` from this directory.

# HPCPerfStats

We provide a standard RPM spec file, to be built using `rpmbuild`. This was
tested with HPCPerfStats 2.4.