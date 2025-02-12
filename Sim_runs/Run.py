import sys
from os.path import isfile
import subprocess
from pathlib import Path

rank = sys.argv[1]

foldername_0 = 'outputfiles'
foldername_1 = 'inputfiles'

if not Path(foldername_0).is_dir():
	Path(foldername_0).mkdir()

if not Path(foldername_1).is_dir():
	Path(foldername_1).mkdir()

restart_flag = 0

start_rank = rank

import numpy as np

promoter_flag = [0]
GQ_on_val = [1.0]
eR_on_val = [ 0.5]
eR_off_val = [0.00001]
topo_val = [100.0]
PQS_flag = [0]

submission_count = 0

for plasmid_flag in range(1):
	for promoter_id in range(1):
		for GQ_on_id in range(len(GQ_on_val)):
			for eR_on_id in range(len(eR_on_val)):
				for topo_id in range(len(topo_val)):
					for eR_off_id in range(len(eR_off_val)):
						for PQS_id in range(len(PQS_flag)):
							folder_0 = 'outputfiles/RUN_' + str(plasmid_flag) + '_' + str(promoter_flag[promoter_id]) + '_' + str(GQ_on_id) + '_' + str(eR_on_id) + '_' + str(topo_id) + '_' + str(eR_off_id) + '_' + str(PQS_id)
							folder_1 = 'inputfiles/RUN_' + str(plasmid_flag) + '_' + str(promoter_flag[promoter_id]) + '_' + str(GQ_on_id) + '_' + str(eR_on_id) + '_' + str(topo_id) + '_' + str(eR_off_id) + '_' + str(PQS_id)
							if not Path(folder_0).is_dir():
								Path(folder_0).mkdir()
							if not Path(folder_1).is_dir():
								Path(folder_1).mkdir()
							marker_filename = 'outputfiles/RUN_' + str(plasmid_flag) + '_' + str(promoter_flag) + '_' + str(GQ_on_id) + '_' + str(eR_on_id) + '_' + str(topo_id) + '_' + str(eR_off_id) + '_' + str(PQS_flag) + '/rates_0.log'
							if isfile(marker_filename):
								continue
							A = [str(restart_flag), str(plasmid_flag), str(promoter_flag[promoter_id]), str(GQ_on_id), str(GQ_on_val[GQ_on_id]), str(eR_on_id), str(eR_on_val[eR_on_id]), str(topo_id), str(topo_val[topo_id]), str(eR_off_id), str(eR_off_val[eR_off_id]), str(PQS_flag[PQS_id]), str(start_rank)]
							ss=' '.join(A)
							print(f'mpirun ./Run_sim configs/test.config', ss)  
       
							slurm_out = subprocess.run(['mpirun', './Run_Sim_bin', 'configs/test.config', str(restart_flag), str(plasmid_flag), str(promoter_flag[promoter_id]), str(GQ_on_id), str(GQ_on_val[GQ_on_id]), str(eR_on_id), str(eR_on_val[eR_on_id]), str(topo_id), str(topo_val[topo_id]), str(eR_off_id), str(eR_off_val[eR_off_id]), str(PQS_flag[PQS_id]), str(start_rank)], capture_output = True, text = True)
							print(slurm_out.stdout, end = '')
            				
							#submission_count += 1
							if submission_count == 10:
								sys.exit(0)
