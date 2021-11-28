# File info here ...

# Import numpy library for use in ...
import numpy as np
# Import os library for use in ...
import os

# Function info here ...
def import_fa(file_name, return_labels=False):
    # List storage for file contents (sequences) and sequene labels
    sequences = []
    labels = []
    # Try to open the file as read only
    try:
        file = open(file_name, "r")
    # If the file would not open, print error message and exit
    except:
        print("\nError: Could not open file")
        print("File name given: "+file_name+"\n")
        raise SystemExit
    # Iterate over all the lines in the file
    for line in file.readlines():
        # If this character is at the start of the line, it is a sequence label
        if line[0] == ">":
            # If the argument 'return_labels' is True, append the label to a list
            if return_labels:
                labels.append(str(line)[1:-1])
            else:
                continue
        # Append the sequence to the list of sequences
        sequences.append(str(line)[:-1])
    # If the argument 'return_labels' is True, return arrays of the sequences and labels
    if return_labels:
        return np.array(sequences), np.array(labels)
    # If False, only return an array of the sequences
    else:
        return np.array(sequences)

# Function info here ...
def import_folder(folder_path, return_names=False):
    print("Reading contents of folder: "+folder_path)
    # List storage for files and file names
    files = []
    file_names = []
    # Try read the directory contents to a list
    try:
        directory_contents = os.listdir(folder_path)
    # If directory is not found, print error message and exit
    except:
        print("\nError: Could not open directory")
        print("Directory path given: "+folder_path+"\n")
        raise SystemExit
    # Iterate over all files in the given directory
    for file in directory_contents:
        # Only read files with the .fa extension
        if ".fa" in file:
            print("  "+file)
            # Call the import_fa() function to read the fasta file
            # This function returns the sequences in the fasta file
            # Here the argument 'return_labels' is left as default=False
            files.append(import_fa(folder_path+'\\'+file))
            # Add the file contents to the list
            file_names.append(file)
        else:
            continue
    # If the argument 'return_names' is True, return arrays of file contents and file names
    if return_names:
        return np.array(files, dtype=object), np.array(file_names)
    # If False, only return a 2D array of the contents of the files
    else:
        return np.array(files, dtype=object)