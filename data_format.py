# File info here ...

# Import numpy library for use in ...
import numpy as np
# Import os library for use in ...
import os
# Import matplotlib.pyplot for use in ...
import matplotlib.pyplot as plt

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
def raw_to_features(data,balance=False,resample=1.0):
    print("\nConverting to features:")
    n = len(data)
    # Find basic data stats for function use:
    #   the max length sequence in the data
    #   the number of classes
    #   count of each class
    max_seq_len = 0
    class_counts = [0]
    num_classes = -1
    # Iterate over all sequences
    for line in data:
        # Look out for a new class
        if "class" in line:
            class_counts.append(1)
            num_classes += 1
            continue
        # Update max sequence length
        if len(line) > max_seq_len:
            max_seq_len = len(line)
        # Update class counts
        class_counts[num_classes+1] += 1
    
    # Since this was -1 based, increment to convert to 0 based count
    num_classes += 1
    
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
    for i in range(num_classes):
        data_by_class.append( data[class_counts[i]:class_counts[i+1]] )
    
    # Instantiate storage of features and labels
    X = []
    y = []
    
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
            # Pull instances
            for i in range(num_classes):
                for j in range(1,total_per_class+1): 
                    X.append( data_by_class[i][j] )
            # Pull labels
            for i in range(num_classes):
                for j in range(total_per_class):
                    y.append(i)
        # If imbalanced class counts are acceptable
        else:
            # Calculate the total number of instances per class in the same ratio as class counts
            total_per_class = [int(num_samples*class_counts[i+1]/n) for i in range(num_classes)]
            # Pull instances
            for i in range(num_classes):
                for j in range(total_per_class[i]+1,total_per_class[i+1]+1):
                    X.append( data_by_class[i][j] )
            # Pull labels
            for i in range(num_classes):
                for j in range(total_per_class):
                    y.append(i)
        print("  Resampling:")
        print("    Total samples:",num_samples)
        print("    Total/class  :",total_per_class)
        print()
    # If not resampling
    # TODO:  Complete - could the above be used instead of conditional?
    else:
        total_per_class = int(n/num_classes)
    
    # Convert from strings to arrays and pad the sequences with zeros to 
    # the length of the maximum length sequence; this is the number of features
    for i in range(len(X)):
        # Instantiate new array of zeros
        new_instance = [0 for i in range(max_seq_len)]
        # Fill in sequence
        for j in range(len(X[i])):
            new_instance[j] = X[i][j]
        # Store new sequence in features store X
        X[i] = new_instance

    # Return features and labels
    return X,y
    """# Instantiate new data storage
    X = np.zeros((num_samples,max_seq_len), dtype=np.object_)
    y = np.zeros(num_samples)      # This implies that there are always 2 classes
    # Iterate over the data filling in X and y
    class_val = -1
    X_line = 0
    line = 0
    class_count = 0
    while line < n:
        # TODO: Track and print progress
        #if line%(n/100)==0:
        #    print(str(line/n*100)+"%",end="\r")
        # Assign the class value
        if "class" in data[line]:
            class_val = int(data[line][-1])
            line+=1
            class_count += 1
            continue
        # If the class quota is met, then continue to next class
        if class_counts[class_val] == total_per_class:
                if class_count == num_classes:
                    break
                while line < n and "class" not in data[line]:
                    line += 1
                continue
        # Fill in the data instance, and pad it with zeros
        class_counts[class_val] += 1
        m = len(data[line])
        for char in range(max_seq_len):
            if char < m:
                X[X_line][char] = data[line][char]
            else:
                X[X_line][char] = 0
        y[X_line] = int(class_val)
        X_line += 1
        # loop increment
        line += 1
    print()"""

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