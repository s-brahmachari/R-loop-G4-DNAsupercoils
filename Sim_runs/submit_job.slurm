#!/bin/bash
#SBATCH --job-name=te_to
#SBATCH --partition=ctbp-common
#SBATCH --account=ctbp-common
#SBATCH --ntasks=32
#SBATCH --constraint="ivybridge"
#SBATCH --mem-per-cpu=2G
#SBATCH --time=07:59:59

module purge
module load GCC/12.2.0 OpenMPI/4.1.5

mpirun ./Run_sim $1 $2 $3 $4 $5 $6 $7 $8 $9 ${10} ${11} ${12}

echo $SLURM_JOB_NODELIST
