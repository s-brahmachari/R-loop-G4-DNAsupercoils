# R-loop-G4-DNAsupercoils

## Compiling the code:

cd code

mpic++ -std=c++11 -O3 Run_Simulation.cpp -o Run_Sim_bin

## Running the compiled binary file:

cd Sim_runs

python Run.py 0

Set the parameters in the script Run.py inside the directory Sim_runs. 
This script creates the folders "inputfiles" and "outputfiles" and sub-directories "RUN_..." corresponding to each parameter set, and then executes the compiled binary. 
Run.py uses mpirun to generate multiple replicas where the cmd line argument is the index for naming the first replica.

Note: the location of the configs/ and torque_interp/ directories with respect to the executable binary is important!

## Analysis

cd analysis

use analyze.py to process simulation trajectories and generate promoter supercoiling files.
Use plot_Txp_Roop_G4.ipynb and plot_promoter_supercoiling.ipynb to further analyze and plot the simulation trajectories.
