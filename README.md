### Ubiquitin Ligase Classification

This is a work in progress. So far I am working on data formatting in data_format.py and have the testing for this embedded on UBL.py. 

I have a basic implementation for a 2D Convolutional Neural Network (in the notebook 2D_CNN.ipynb) to classify UBL proteins in contrast to a set of other non-UBL proteins, and hopefully thereafter to a set of known false-positive non-UBLs.

So far the data is formatted to:
  * convert the amino acids in the sequences as integer values
  * remove any characters after the 2000th index (for the sake of testing the model training process)
  * split the sequences into two using the numpy reshape function
    * for the time being this simulates 2 features where there will be a more than one

The CNN has some toy layers for now merely for the sake of testing. These will be adjusted in time.

Initial results on this first test version of the workflow are to be posted later today (Sat Dec 4).

More info coming soon...

To read more about a previous attempt at UBL classification, see https://peerj.com/articles/7055.pdf

&copy; Chris Burgoyne 2021