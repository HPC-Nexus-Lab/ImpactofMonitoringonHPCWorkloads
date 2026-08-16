#! /bin/bash

set -xe

prefix=/usr

CONF_ARGS="--disable-static \
--prefix=$prefix \
--with-pkglibdir=ovis-ldms \
--disable-doc \
--disable-doc-html \
--enable-ovis_auth \
--enable-ovis_event \
--enable-zap \
--enable-sock \
--disable-rdma \
--disable-mmap \
--disable-readline \
--enable-ldms-python \
--enable-python \
--enable-flatfile \
--enable-csv \
--enable-store \
--disable-rabbitv3 \
--disable-rabbitkw \
--disable-cray_power_sampler \
--disable-cray_system_sampler \
--disable-aries-gpcdr \
--disable-gpcdlocal \
--disable-aries-mmr \
--disable-ugni \
--disable-perfevent \
--disable-procdiskstats \
--disable-atasmart \
--disable-generic_sampler \
--enable-dstat \
--enable-llnl-edac \
--disable-opa2 \
--disable-perf \
--disable-ibnet \
--disable-jobid \
--enable-array_example \
--enable-procinterrupts \
--enable-procnetdev \
--enable-procnfs \
--enable-procstat \
--enable-vmstat \
--enable-meminfo \
--enable-lustre \
--enable-slurmtest \
--enable-filesingle"

#--disable-doc-latex \
#--disable-doc-man \
#--disable-doc-graph \


#[ ! -e distribution/README.md ] && git clone https://github.com/ovis-hpc/distribution.git distribution

#rm -rf LDMS
mkdir -p ldms

[ ! -e ldms/INSTALL ] && git clone https://github.com/ovis-hpc/ovis.git ldms

cd ldms
git checkout v4.5.2

./autogen.sh
./configure $CONF_ARGS
make dist

cp ovis-ldms-*.gz ~/rpmbuild/SOURCES

./config.status --file=../ldms.spec:../ldms.spec.in

rpmbuild --define "_version 4.5.2" --define "ldmssuffix %{nil}" --define "ldmsrelease 1" -ba ../ldms.spec
