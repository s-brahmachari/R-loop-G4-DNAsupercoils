import os
import numpy as np

path = "/scratch/sb95/R-loop/Runs_eRoff/sig-0.06/outputfiles/"
for directory in os.listdir(path):
    print(directory)
    for fname in os.listdir(os.path.join(path,directory)):
        if "sigma" in fname and "synced" not in fname and "spot" not in fname and "prom" not in fname and "gene" not in fname:
            
            fprom = open(os.path.join(path, directory, "prom"+fname), 'w')
            # fgene = open(os.path.join(path, directory, "gene"+fname), 'w')
            print(fname)
            with open(os.path.join(path, directory, fname), 'r') as fsig:
                for line in fsig:
                    row = line.strip().split('\t')
                    try:
                        fprom.write(f"{row[0]}\t {row[-1]}\t {row[1]}\n")
                        if len(row)>3: 
                            # print(row[1:-1])
                            sc = np.mean(np.array(row[1:-1]), dtype=float)
                            # fgene.write(f"{row[0]}\t {row[2]}\n")
                    except(IndexError):
                        pass
                    # time = row[0]
                    # prom_sc = row[-1]
                    # print(time, prom_sc)
                    # sys.exit()
                    # break
            fprom.close()
            # fgene.close()
