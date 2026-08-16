#!/bin/bash
#SBATCH --job-name="rfm_hpl_test_4ad6f573"
#SBATCH --ntasks=56
#SBATCH --cpus-per-task=1
#SBATCH --output=rfm_job.out
#SBATCH --error=rfm_job.err
#SBATCH --time=0:15:0
srun --cpus-per-task=1 --mpi=pmix bin/Linux_Intel64/xhpl --dat ./HPL.dat
