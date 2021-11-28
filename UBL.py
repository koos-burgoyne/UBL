# import ...
import data_format as format
import numpy as np
import sys

import sklearn

def main():
    #if len(sys.argv)==2:
    if len(sys.argv)==1:
        #sequences = format.import_fa(sys.argv[1])
        sequences = format.import_fa("pos-ubl.fa")
        files = format.import_folder(r"E:\Chris\comp_bio\ubl-data\data")
        
    else:
        print("Error: 1 arg required <filename>, "+str(len(sys.argv)-1)+" args given")
        print("Usage: python3 main.py <filename>")
        quit()
    return

if __name__ == "__main__":
    main()