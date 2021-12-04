## Ubiquitin Ligase Classification

This is a work in progress. So far I am working on data formatting in data_format.py and have the testing for this embedded on UBL.py. 

I have a basic implementation for a 2D Convolutional Neural Network (in the notebook 2D_CNN.ipynb) to classify UBL proteins in contrast to a set of other non-UBL proteins, and hopefully thereafter to a set of known false-positive non-UBLs.

### Current Status
I know, this repo is currently a mess... but I will sort that out now that I have got some working code and an idea of where this is going.

So far the data is formatted to:
  * convert the amino acids in the sequences to integer values
  * remove values after the 2000th index (for the sake of testing the model training process)
  * split the sequences into two using the numpy reshape function
    * for the time being there is only one feature (the characters of the sequence), whereas this split simulates 2 features where there will be more than one in the future

The functionality of inferring features from the sequence will be added in a local python library file following a similar paradigm to the McDermott et al. paper referened below.

The CNN has some arbitrarily selected layers for now merely for the sake of testing. These will be thoughtfully adjusted in time.

The data was split 80:20 into modelling/validation data, and the modelling data was then split again 80:20 into train:test

#### Initial Results
From today's (Dec4,21) testing on a toy version of the dataset with arbitrary model layers:
  * Model train time    : 1hr 25min (255s/epoch, 8s/step)
  * Final Train Accuracy: 92.2%
  * Final Test Accuracy : 79.42%
  * Validation Accuracy : 83.03%

![Classification percent accuracy by epoch](/assets/accuracy_dec4.png "Classification percent accuracy by epoch")

It seems possible that with a well planned model, more training epochs, and a properly formatted dataset, this method has the potential to perform the required task.

### More
More information on the workflow and other aspects of this project will be coming soon...

To read more about a previous attempt at UBL classification, see McDermott et al. 2019: https://peerj.com/articles/7055.pdf

&copy; Chris Burgoyne 2021