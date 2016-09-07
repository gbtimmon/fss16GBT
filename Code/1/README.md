#Homework - Week1

##Example eg0
eg0 initially prints only the 'attributes' in the dataset. Then, it prunes content of the dataset using the 'gawk' '-F' and 'NF==5' to select the columns, and removes and ',' separator. It also Alphabetically sorts the data, formats it and then prints it out. Finally eg0 prints a decision tree formed by using j48.

##Example eg1
eg1 prints the contents of the the dataset with the same contraints as eg0.

##Example eg2
eg2 uses the j48 learner on the dataset with cross validation. The decision tree from the j48 algorithm, its confusion matrix and various statistics are printed. Also, line numbers are added while printing.

##Example eg3
It performs the j48 algorithm with the same dataset for the training data and test data.This causes the predition to be a 100%. Here, all the predictions are shown to be 1.

##Example eg4
eg4 calls the eg3 function with 'wantgot' piped. Wantgot makes the results clearer and shows the 100% results of the previous function, when comparing the j48 prediction and the actual data.

##Example eg5
eg5 calls the eg4 function with another function 'abcd'. abcd prints out results where a:true negatives, b:false negatives, c:false positives, and d:true positives values are calculated. Since our training data and test set are the same, we see a 100% result here as well.

##Example eg6
The crossval function takes arguments 1 and 3 for the number of crossvals and data sets needed to divide into the training and test data.The two algorithms j48 and jrip are run.The stratified crossval divides data into 3 parts and uses 2 of them for training and one for testing randomly. Because of this, the algorithms run 3 times. Also it is observed that the results for the 3 iterations are different.

##Example eg7
This runs the j48 and jrip algorithms 5 times each and cross validates 5 times. Similar to eg6, the data is divided into 5 parts and used randomly for test and training data. The results for this prediction go into a temporary 'out' file. It also stors the precision and recall values for each algorithm in separate files.

##Example eg8
eg8 is similar to the previous example, but it saves the recall and precision using the column names instead of gawk, so its easier to read.

##Example eg9
The output from eg8 is used for eg9. This compares the two algorithms by using statistics on which percentile the recall and fall-out rates fall in. It separates the stored results and execution so the results can be seen anytime.

##Example eg10
This function uses 5 learners: j48, jrip, nb, rbfnet, bnet. It uses the dataset jedit-4.1.arff and stores recall and precision for all 5 algorithms. The statistics are calculted again and the algorithms are ranked.
