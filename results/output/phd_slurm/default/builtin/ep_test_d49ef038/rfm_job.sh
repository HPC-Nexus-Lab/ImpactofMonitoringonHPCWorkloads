#!/bin/bash
#SBATCH --job-name="rfm_ep_test_d49ef038"
#SBATCH --ntasks=56
#SBATCH --cpus-per-task=1
#SBATCH --output=rfm_job.out
#SBATCH --error=rfm_job.err
#SBATCH --time=0:15:0
srun --cpus-per-task=1 --mpi=pmix bin/ep.E.x
