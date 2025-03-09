# R-loop-G4-DNAsupercoils

## Overview
This repository contains a computational model to simulate the coupling of RNA Polymerase (RNAP) recruitment and translocation with DNA supercoiling. The model captures the interplay between transcription, transient R-loop formation, G-quadruplex (G4) structures, and their effects on promoter supercoiling and transcription regulation. The simulation explores how the dynamic interactions between these elements influence transcription initiation and suppression.

<img src="images/model_schematic.png" alt="Model Schematic" width="400">

## Model Description
The model simulates a negatively supercoiled plasmid with a single gene and considers the following key processes:
- **Transcription Initiation**: RNAP recruitment depends on the promoter's supercoiling density, modeled using a sigmoidal function.
- **R-loop Formation**: A transient R-loop (tRloop) forms during transcription, which may transition into a Stable R-loop that absorbs DNA supercoils and suppresses transcription.
- **G4 Structure Formation**: If G4-forming sequences (PQS) are present, the transient R-loop can nucleate a G4 state, stabilizing the R-loop and further repressing transcription.
- **Supercoiling Dynamics**: The model includes plectoneme relaxation events to simulate supercoiling redistribution along the DNA.
- **Parameter Tuning**: The model explores different rates of R-loop and G4 formation to identify transcriptional suppression regimes.

For detailed theoretical background and comparison with experimental observations, refer to the model documentation.

## Installation & Compilation
### Prerequisites
Ensure you have the following installed:
- C++ compiler with MPI support (e.g., `mpic++`)
- Python 3.x
- Required Python packages: `numpy`, `matplotlib`, `pandas`

### Compiling the Code
Navigate to the `code/` directory and compile the simulation code:
```sh
cd code
mpic++ -std=c++11 -O3 Run_Simulation.cpp -o Run_Sim_bin
```

## Running Simulations
### Execution
Navigate to the `Sim_runs/` directory and execute the compiled binary using the provided Python script:
```sh
cd Sim_runs
python Run.py 0
```

### Parameter Configuration
Modify `Run.py` inside `Sim_runs/` to set the desired simulation parameters. This script will:
- Create `inputfiles/` and `outputfiles/` directories.
- Generate subdirectories (`RUN_...`) for each parameter set.
- Execute the compiled simulation binary.
- Use `mpirun` to run multiple replicas, where the command-line argument specifies the first replica’s index.

**Note**: The relative paths to the `configs/` and `torque_interp/` directories must be maintained with respect to the executable binary.

## Analysis & Visualization
### Processing Simulation Data
To analyze the generated simulation trajectories, navigate to the `analysis/` directory:
```sh
cd analysis
python analyze.py
```

### Visualization
The following scripts can be used for plotting:
- **`plot_Txp_Rloop_G4.ipynb`**: Analyzes and visualizes transcription and R-loop/G4 formation dynamics.
- **`plot_promoter_supercoiling.ipynb`**: Generates plots showing the evolution of promoter supercoiling.

## References
DNA supercoiling-mediated G4/R-loop formation
tunes transcription by controlling the access of RNA
polymerase (Hwang et al. 2024) https://doi.org/10.21203/rs.3.rs-4405653/v1
## Contact
For questions or contributions, please reach out to the repository maintainers.

