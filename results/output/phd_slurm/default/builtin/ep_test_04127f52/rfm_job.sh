#!/bin/bash
#SBATCH --job-name="rfm_ep_test_04127f52"
#SBATCH --ntasks=56
#SBATCH --cpus-per-task=1
#SBATCH --output=rfm_job.out
#SBATCH --error=rfm_job.err
pwd
whoami
~/phd/reframe/disable_procs.sh 56
srun --cpus-per-task=1 --mpi=pmix bin/ep.D.x
~/phd/reframe/enable_procs.sh
