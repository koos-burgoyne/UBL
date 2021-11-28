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
    print("    "+str(len(sequences))+" sequences")
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
    # Return object type array to allow for ragged array
    # If the argument 'return_names' is True, return arrays of file contents and file names
    if return_names:
        return np.array(files, dtype=object), np.array(file_names)
    # If False, only return a 2D array of the contents of the files
    else:
        return np.array(files, dtype=object)

# Function info here ...
def sequences_to_features(sequences):
    # The set of features to convert the sequence to
    feature_lib = {}
    feature_lib["feat1"] = {}
    feature_lib["feat2"] = {}
    num_features = len(feature_lib.keys)
    # Initialize storage for the new list of features
    features = [[] for i in range(num_features)]
    # Iterate over all sequences in 'sequences' array
    for i,seq in enumerate(sequences):
        # Iterate over all nucleotides in a sequence
        for j in seq:
            # Iterate over all features
            for k,feature in enumerate(feature_lib.items()):
                features[i].append()
    # Return object type array to allow for ragged array
    return np.array(features, dtype=object)

# Function info here ...
def pad_features(X):
    # Find the maximum length of sequence
    max_len_seq = 0
    for i in range(len(X)):
        if len(X[i]) > max_len_seq:
            max_len_seq = len(X[i])
    # Create a new array containing the data X padded with zeros so that it is not a ragged array of sequences
    new_X = np.zeros( (len(X),max_len_seq) )
    # Iterate over all sequences in the input
    for i in range(len(X)):
        # Assign the input sequence to the new padded dataset
        seq_len = len(X[i])-1
        new_X[i][:seq_len] = X[i]
    # Return the padded dataset
    return new_X

# Function info here ...
def retrieve_features(files, fnames=None):
    # Storage for new dataset with revised features and labels
    sequences_as_features = []
    labels = []
    # Iterate over all files in the input 'files' array
    for file in files:
        # Iterate over all sequences contained in a file
        for seqs in file:
            # Convert the sequence to an instance of data with new features
            sequences_as_features.append(sequences_to_features(seqs))
    # Return object type array to allow for ragged array
    # If the file names are provided, then the labels can be returned according to the file name each sequence came from
    if fnames is not None:
        return np.array(sequences_as_features, dtype=object), np.array(labels)
    # If the file names are not provided, the data is returned unlabeled
    else:
        return np.array(sequences_as_features, dtype=object)

# Function info here ...
def print_stats(files, file_names):
    print("Data Stats:")
    for file,fname in zip(files,file_names):
        max = 0
        min = 1e6
        mean_length = 0
        print("  "+fname)
        for sequence in file:
            seq_len = len(sequence)
            if seq_len > max:
                max = seq_len
            if seq_len < min:
                min = seq_len
            mean_length += seq_len
        mean_length /= len(file)
        std_dev = 0
        for sequence in file:
            std_dev += (mean_length - len(sequence))**2
        print("    Min : "+str(min))
        print("    Max : "+str(max))
        print("    Mean: "+str(round(mean_length,3)))
        print("    StdD: "+str(round(np.sqrt(std_dev/(len(file)-1)),3)))