# File info here ...

# Import numpy library for use in ...
import numpy as np
import os

# Function info here ...
def import_fa(file_name, return_labels=False):
    sequences = []
    labels = []
    file = open(file_name, "r")
    for line in file.readlines():
        if ">" in line:
            if return_labels:
                labels.append(str(line)[1:-1])
            else:
                continue
        sequences.append(str(line)[:-1])
    if return_labels:
        return np.array(sequences), np.array(labels)
    else:
        return np.array(sequences)

# Function info here ...
def import_folder(folder_path, return_names=False):
    files = []
    file_names = []
    for file in os.listdir(folder_path):
        print(file)
        if "fa" in file:
            files.append(import_fa(file))
            file_names.append(file)
        else:
            continue
    if return_names:
        return np.array(files, dtype=object), np.array(file_names)
    else:
        return np.array(files, dtype=object)