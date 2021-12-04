# import ...
import data_format as format
import sys

def main():
    # Check if number of arguments is correct
    # The 0th argument is the executable name
    # The 1st is whether to read a file or folder
    # The 2nd is the file/folder name
    if len(sys.argv)==3:
        
        # If the first argument is "file", call the import_fa() function to retrieve the sequences
        if sys.argv[1] == "file":
            data = format.import_fa(sys.argv[2])
            X, y = format.raw_to_features(data,balance=True,resample=0.01)
            #print(X[0:2])
            #print(y[0:2])

        # If the first argument is "folder", read the .fa files in the given folder
        elif sys.argv[1] == "folder":
            folder_contents,file_names = format.import_folder(sys.argv[2], return_names=True)
            format.print_stats(folder_contents,file_names,plot=True)
            #X, y = format.retrieve_features(folder_contents,fnames=file_names)

        # If the first argument is neither 'file' nor 'folder', print error message and exit
        else:
            print("Error: first argument must be 'file' or 'folder'")
            for i,arg in enumerate(sys.argv):
                if i > 0:
                    print("  arg "+str(i)+": "+sys.argv[i])
            print("Usage: python3 main.py <file/folder> <filename>")
            sys.exit()
    
    # If the incorrect number of arguments is given, print error and exit
    else:
        print("Error: 2 args required, "+str(len(sys.argv)-1)+" args given")
        for i,arg in enumerate(sys.argv):
            if i > 0:
                print("  arg "+str(i)+": "+sys.argv[i])
        print("Usage: python3 main.py <file/folder> <filename>")
        sys.exit()

    return

if __name__ == "__main__":
    main()