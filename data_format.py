# File info here ...

import numpy as np
import os
import matplotlib.pyplot as plt

amino_acids = {
    "A":0, "R":1, "N":2, "D":3, "C":4, "Q":5, "E":6, "G":7, "H":8, "I":9, "L":10, "K":11, "M":12, "F":13, "P":14, "S":15, "T":16, "W":17, "Y":18, "V":19
}

VHSE_descriptors = {
    0:{"A":0.15, "R":-1.47, "N":-0.99, "D":-1.15, "C":0.18, "Q":-.96, "E":-1.18, "G":-0.2, "H":-0.43, "I":1.27, "L":11.36, "K":-1.17, "M":1.01, "F":1.52, "P":0.22, "S":-0.67, "T":-0.34, "W":1.5, "Y":0.61, "V":0.76},
    1:{"A":-1.11, "R":1.45, "N":0,     "D":0.67, "C":-1.67, "Q":0.12, "E":0.4, "G":-1.53, "H":-0.25, "I":-0.14, "L":0.07, "K":0.7, "M":-0.53, "F":0.61, "P":-0.17, "S":-0.86, "T":-0.51, "W":2.06, "Y":1.6, "V":-0.92},
    2:{"A":-1.35, "R":1.24, "N":-0.37, "D":-0.41, "C":-0.46, "Q":0.18, "E":0.1, "G":-2.63, "H":0.37, "I":0.3, "L":0.26, "K":0.7, "M":0.43, "F":0.96, "P":-0.5, "S":-1.07, "T":-0.55, "W":1.79, "Y":1.17, "V":0.17},
    3:{"A":-0.92, "R":1.27, "N":0.69, "D":-0.01, "C":-.021, "Q":0.16, "E":0.36, "G":2.28, "H":0.19, "I":-1.8, "L":-0.8, "K":0.8, "M":0, "F":-0.16, "P":0.05, "S":-0.41, "T":-1.06, "W":0.75, "Y":0.73, "V":-1.91},
    4:{"A":0.02, "R":1.55, "N":-0.55, "D":-2.68, "C":0, "Q":0.09, "E":-2.16, "G":-0.53, "H":0.51, "I":0.3, "L":0.22, "K":1.64, "M":0.23, "F":0.25, "P":-0.01, "S":-0.32, "T":0.01, "W":0.75, "Y":0.53, "V":0.22},
    5:{"A":-0.91, "R":1.47, "N":0.85, "D":1.31, "C":1.2, "Q":0.42, "E":-0.17, "G":-1.18, "H":1.28, "I":-1.61, "L":-1.37, "K":0.67, "M":0.1, "F":0.28, "P":-1.43, "S":0.27, "T":-0.01, "W":-0.13, "Y":0.25, "V":-1.4},
    6:{"A":0.36, "R":1.3, "N":0.73, "D":0.03, "C":-1.61, "Q":-0.2, "E":0.91, "G":2.01, "H":0.93, "I":-0.16, "L":0.08, "K":1.63, "M":-0.86, "F":-1.33, "P":-0.19, "S":-0.64, "T":-0.79, "W":-1.06, "Y":-0.96, "V":-0.24},
    7:{"A":-0.48, "R":0.83, "N":-0.8, "D":0.56, "C":-0.19, "Q":-0.41, "E":0.02, "G":-1.34, "H":0.65, "I":-0.13, "L":-0.62, "K":0.13, "M":-0.68, "F":-0.2, "P":3.56, "S":0.11, "T":0.39, "W":-0.85, "Y":-0.52, "V":-0.03}
}

# Function info here ...
def import_fa(file_name, return_labels=False):
    print("Importing "+file_name)
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
    print("\nReading contents of folder: "+folder_path)
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
def raw_to_features(data,resample=1.0,balance=False):
    print("\nConverting to features:")
    num_VHSE = len(VHSE_descriptors)
    num_AA = len(amino_acids)
    num_features = num_AA + num_VHSE
    n = len(data)
    # Find basic data stats for function use:
    #   the max length sequence in the data
    #   the number of classes
    #   count of each class
    max_seq_len = 0
    class_counts = [0]
    num_classes = -1
    # Iterate over all sequences to count num classes, class frequencies, and the max sequence length
    for line in data:
        # Look out for a new class
        if "class" in line:
            class_counts.append(0)
            num_classes += 1
            continue
        # Skip labels
        elif line[0] == ">":
            continue
        # Update max sequence length
        if len(line) > max_seq_len:
            max_seq_len = len(line)
        # Update class counts
        class_counts[num_classes+1] += 1
    
    # Since this was -1 based, increment to convert to 0 based count
    num_classes += 1
    n -= num_classes
    
    # Print stats found above
    print("  Num Classes:", num_classes)
    print("  Class Counts:")
    frmt = "{:>7}"*num_classes
    print(" "+frmt.format(*[i for i in range(num_classes)]))
    print("   ",end="")
    frmt = "{:>7}"*num_classes
    print(" "+frmt.format(*[class_counts[i] for i in range(1,num_classes+1)]))

    # Split data by class for resampling
    data_by_class = []
    start_idx = 1
    end_idx = start_idx + class_counts[1]
    for i in range(num_classes):
        new_class = data[start_idx+1:end_idx]
        np.random.shuffle(new_class)
        data_by_class.append( new_class )
        if i < num_classes-1:
          #print(start_idx, end_idx, class_counts[i+2], class_counts)
          start_idx += end_idx
          end_idx = start_idx + class_counts[i+2]

    #print("data by class:",data_by_class)

    # Init variables for resampling
    total_per_class = 0
    num_samples = n
    # If resampling:
    if resample != 1.0:
        # Calculate the size of the resampled dataset
        num_samples = int(n*resample)
        # If balanced classs coutns are required:
        if balance:
            # Calculate a balanced total number of instances per class
            total_per_class = int(num_samples/num_classes)
            if total_per_class > min(np.array(class_counts)[1:]):
                total_per_class = min(np.array(class_counts)[1:])
            #print("\ntotal/class:", total_per_class, "\n")
            for i in range(len(data_by_class)):
                indexes = np.random.default_rng().choice(len(data_by_class[i]), size=total_per_class-1, replace=False)
                #print("idxs:",indexes)
                data_by_class[i] = data_by_class[i][indexes]
            
        # If imbalanced class counts are acceptable
        else:
            # Calculate the total number of instances per class in the same ratio as class counts
            total_per_class = [int(num_samples*class_counts[i+1]/n) for i in range(num_classes)]
            #print("total/class:",total_per_class)
            for i in range(len(data_by_class)):
                indexes = np.random.default_rng().choice(len(data_by_class[i]), size=total_per_class[i]-1, replace=False)
                data_by_class[i] = data_by_class[i][indexes]
            
        print("  Resampling:")
        print("    Dataset size :",n)
        print("    Total/class  :",total_per_class)
        print("    Total samples:",total_per_class*num_classes)
        print()
    # If not resampling
    # TODO:  Complete - could the above be used instead of conditional?
    else:
        total_per_class = int(n/num_classes)
    
    #print("data by class:",data_by_class)
    
    # Instantiate storage of features and labels
    X = []
    y = []
      
    # Convert from strings to arrays and pad the sequences with zeros to 
    # the length of the maximum length sequence; this is the number of features
    index = 0
    for i in range(len(data_by_class)):
        for j in range(len(data_by_class[i])):
            # Instantiate new array of zeros
            new_instance = []
            for k in range(num_VHSE):
                new_instance.append([-999 for acid in range(max_seq_len)])
            for k in range(num_AA):
                new_instance.append([0 for acid in range(max_seq_len)])
            # Fill in sequence
            for k in range(len(data_by_class[i][j])):
                acid_char = data_by_class[i][j][k]
                if acid_char in amino_acids:
                    for l in range(num_VHSE):
                        new_instance[l][k] = VHSE_descriptors[l][acid_char]
                    new_instance[amino_acids[acid_char]+num_VHSE][k] = 1
            # Store new sequence in features store X
            X.append(new_instance)
            y.append(i)
            index += 1

    # Return features and labels
    return np.array(X),np.array(y),max_seq_len

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
        # Iterate over all amino_acids in a sequence
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
def plot_acid_proportions(amino_acids, total_char):
    num_ticks = 0
    keys = None
    # Get the keys and number of keys for plotting
    for fname,dict in amino_acids.items():
        num_ticks = len(dict)
        keys = dict.keys()
        break
    # Plotting variables
    xtick_loc = np.linspace(1,num_ticks*4,num_ticks)
    width = 0.9
    plt.figure()
    idx_counter = 0
    for fname,dict in amino_acids.items():
        for acid in dict:
            dict[acid] /= total_char[idx_counter]
        plt.bar(xtick_loc+idx_counter*width, dict.values(), label=fname)
        idx_counter += 1
    plt.ylabel("Proportion of Total Amino Acids")
    plt.xlabel("Amino Acids")
    xtick_loc = np.linspace(1,num_ticks*4,num_ticks)
    plt.xticks(xtick_loc+width, keys)
    plt.legend()
    plt.show()
    return

# Function info here ...
def print_stats(files, file_names, print_acid_prop=False, plot=False):
    print("\nData Stats:")
    amino_acids = {}
    total_char = np.zeros(len(files))
    idx_counter = 0
    # Iterate over all files in the input array 'files', along with the corresponding file names
    for file,fname in zip(files,file_names):
        # If on the first file, start a new dictionary to store acidleotide counts
        if len(amino_acids) == 0:
            amino_acids[fname] = {}
        # If on a subsequent file, copy the previous files dictionary
        # This ensures the same amino_acids are covered in the same order
        # Set the counts to 0 for this file
        else:
            prev_fname = list(amino_acids)[-1]
            amino_acids[fname] = amino_acids[prev_fname].copy()
            for acid in amino_acids[fname]:
                amino_acids[fname][acid] = 0
        # Function variables for computing stats
        fname_dict = amino_acids[fname]
        max = 0
        min = 1e6
        mean_length = 0
        print("  "+fname)
        # Across all sequences, find the min and max length sequences,
        # count the occurrences of each amino acid, and find the mean
        # and standard deviation of all sequence lengths in this file. 
        for sequence in file:
            seq_len = len(sequence)
            if seq_len < min:
                min = seq_len
            if seq_len > max:
                max = seq_len
            mean_length += seq_len
            total_char[idx_counter] += seq_len
            for acid in sequence:
                if acid not in fname_dict:
                    fname_dict[acid] = 0
                else:
                    fname_dict[acid] += 1
        mean_length /= len(file)
        std_dev = 0
        for sequence in file:
            std_dev += (mean_length - len(sequence))**2
        # Print the basic stats
        print("    Min : "+str(min))
        print("    Max : "+str(max))
        print("    Mean: "+str(round(mean_length,3)))
        print("    StdD: "+str(round(np.sqrt(std_dev/(len(file)-1)),3)))
        # If argument is True, print amino acid proportions
        if print_acid_prop:
            print("    amino_acids Porportion of Occurence:")
            for acid,count in fname_dict.items():
                print("        "+acid+": "+str(round(fname_dict[acid]/total_char[idx_counter],3)))
        idx_counter += 1
    print()
    # Plot amino acid proportions of all files contained in the input array 'files'
    if plot:
        plot_acid_proportions(amino_acids, total_char)
    return