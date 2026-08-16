#!/bin/bash
#SBATCH --job-name="rfm_ft_test_c65b242e"
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --output=rfm_job.out
#SBATCH --error=rfm_job.err
srun --cpus-per-task=1 --mpi=pmix bin/ft.C.x
