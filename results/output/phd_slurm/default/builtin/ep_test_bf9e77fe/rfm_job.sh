#!/bin/bash
#SBATCH --job-name="rfm_ep_test_bf9e77fe"
#SBATCH --ntasks=56
#SBATCH --cpus-per-task=1
#SBATCH --output=rfm_job.out
#SBATCH --error=rfm_job.err
#SBATCH --time=0:15:0
srun --cpus-per-task=1 --mpi=pmix bin/ep.E.x
