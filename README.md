## Ubiquitin Ligase Classification

This is a work in progress. At this point I have improved on the data formatting in data_format.py and have the testing for this embedded on UBL.py.

I have a basic implementation for a 2D Convolutional Neural Network (in the notebook 2D_CNN.ipynb) to classify UBL proteins in contrast to a set of other non-UBL proteins. 
Given the current result set, I think it's reasonable that the next step should be to include the set of known false-positive non-UBLs as a third class and report on the classification accuracy.

### Current Status
#### Features
After the previous result, which was fairly promising, the data formatting was improved to include the following:
  * convert the amino acids in the sequences to one-hot encoding where each row of 20 rows corresponds to a specific amino acid.
  * add 8 features as specified by Xie et al. 2013
    * they provide a table of 8 VHSE (principal component score vector of hydrophobic, steric, and electronic properties) descriptors.
  * have a final matrix shape of n (maximum protein length in the input set) by 28 (20 rows for one-hot-encoded amino acids and 8 rows for the VHSE descriptors).
This feature extraction is an advance with respect to the previous attempt, and could be improved upon with future iterations.
#### CNN
The CNN remains to be improved upon. In order to get a result without spending enormous time training, the CNN has two convolutional layers with max-pooling, following by flattening and condensing. These are arbitrarily selected layers for now merely for the sake of further testing. These will be thoughtfully adjusted in the future with further iterations of testing and results.
The number of epochs is set at 30 because that 20 was sufficient in the previous test iteration to reveal the trend in validation accuracy while completing the training process in a reasonable amount of time, so this time it was increased to 30 epochs to seek improved accuracy.
The loss function is categorical cross-entropy and the optimizer is Adam.
#### Data Split
In this testing iteration, the data was split 80:20 into modelling/validation data, and the modelling data was then split again 80:20 into train:test.
#### Results
Four models were trained, each on a separate dataset. The four datasets, and the performance of the model trained on them, are set out in the bullet points below. From validation results validating with 6449 samples from the dataset that includes zinc finger negatives, split by the two classes (roughly 1:1), the accuracy of the model in each iteration of testing is:
  * Training data without zinc finger negatives:
    * Unbalanced data, model accuracy: 75.1%
    * Balanced data, model accuracy: 88.77%
  * Training data (balanced) with zinc finger negatives:
    * Accuracy: 76.93% (false positive rate of ~30%)
  * Training data (balanced) with only zinc finger sequences as negatives:
    * Accuracy: 87.16%

![Classification percent accuracy by epoch](/results/test1_acc.png "Classification percent accuracy by epoch")

This figure shows the results of testing without negative sequences that have a zinc finger. The accuracy is quite high and could potentially be improved. It has not yet converged showing that more epochs can improve performance.

With these tests, it seems likely that with a well planned model (or perhaps an ensemble), more training epochs, and a thoughtfully formatted dataset, this method has the potential to perform the required task to a high degree of accuracy.

A more detailed examination of the results is contained in the Testing_report.pdf document in this repository.

### More
To read more about a previous attempt at UBL classification, see:
McDermott, J.E., Cort, J.R., Nakayasu, E.S., Pruneda, J.N., Overall, C. and Adkins, J.N., 2019. Prediction of bacterial E3 ubiquitin ligase effectors using reduced amino acid peptide fingerprinting. PeerJ, 7, p.e7055.
https://peerj.com/articles/7055.pdf

The 8 VHSE features came from this paper: 
Xie, J., Xu, Z., Zhou, S., Pan, X., Cai, S., Yang, L. and Mei, H., 2013. The VHSE-based prediction of proteasomal cleavage sites. PLoS One, 8(9), p.e74506.
The table of features can be viewed at https://www.researchgate.net/figure/VHSE-descriptors-for-20-natural-amino-acids_tbl1_256614499

&copy; Chris Burgoyne 2021