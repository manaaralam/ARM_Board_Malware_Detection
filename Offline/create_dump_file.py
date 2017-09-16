import os
from os import listdir
from os.path import isfile, join
import numpy as np

path_to_log_files = "./log_file_benign/"
path_to_dump_files = "./dump_file_benign/"

path_to_log_malware = "./log_file_malware/"
path_to_dump_malware = "./dump_file_malware/"

indicator = ["ls", "ps", "who", "netstat", "pwd"]
hpc = ["cycles", "instructions", "cache-references", "cache-misses", "branches", "branch-misses"]
iteration = 50

Matrix = [[0 for x in range(len(hpc) * len(indicator))] for y in range(iteration)]
Count = [[0 for x in range(len(hpc))] for y in range(len(indicator))]

def initialize():
    for row in range(iteration):
        for col in range(len(hpc) * len(indicator)):
            Matrix[row][col] = 0
    for row in range(len(indicator)):
        for col in range(len(hpc)):
            Count[row][col] = 0

def create_dump(file):
    if file == "benign":
        log = path_to_log_files
        dump = path_to_dump_files
    if file == "malware":
        log = path_to_log_malware
        dump = path_to_dump_malware
    if not os.path.exists(dump):
        os.makedirs(dump)
    files = [f for f in listdir(log) if isfile(join(log, f))]
    for f in files:
        initialize()
        with open(log+f, "r") as inp:
            content = inp.readlines()
        for item in content:
            item = item.strip()
            if item.startswith("Performance"):
                ind = item.split("'")[1]
                ind_index = indicator.index(ind)
            if item != "" and item[0].isdigit():
                data = item.split()
                h = data[1]
                if h in hpc:
                    hpc_index = hpc.index(h)
                    entry = int(data[0])
                    col = ind_index + len(indicator) * hpc_index
                    row = Count[ind_index][hpc_index]
                    Matrix[row][col] = entry
                    Count[ind_index][hpc_index] += 1
        name = f.split(".")[0]
        np.savetxt(dump+name+".txt", Matrix, fmt = "%0.1f", delimiter = " ")

create_dump("benign")
create_dump("malware")