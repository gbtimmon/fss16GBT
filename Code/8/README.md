## Code 8

Using datasets given by WEKA: contact-lenses.arff, glass.arff, iris.arff, credit-g.arff, hypothyroid.arff, diabetes.arff
Classifier used: Naive Bayes


### Perform feature selection using the J48 M trick

| Dataset from WEKA  | selected features | All features   | Precision-selected | Precision-all | recall-selected | Recall-all |
| ------------- |:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|
|  contact-lenses.arff | 2 | 4  | 0.910 | 0.691  | 0.875 | 0.708 | 
|  glass.arff | 5 | 9 | 0.510 | 0.496 | 0.486 | 0.486 |
|  iris.arff | 1 | 4  | 0.955 | 0.960  | 0.953 | 0.960 | 
|  credit-g.arff  | 9 | 20 | 0.715 | 0.743 | 0.733 | 0.754 | 
|  hypothyroid.arff | 8 | 30 | 0.943 | 0.946 | 0.951 | 0.953 |
|  diabetes.arff |  4 | 8 | 0.761 | 0.759 | 0.767 | 0.763 | 

### Perform wrapper feature selection

| Dataset from WEKA  | selected features | All features   | Precision-selected | Precision-all | recall-selected | Recall-all |
| ------------- |:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|
|  contact-lenses.arff | 2 | 4  | 0.910 | 0.691  | 0.875 | 0.708 | 
|  glass.arff | 4 | 9 | 0.485 | 0.496 | 0.495 | 0.486 |
|  iris.arff | 1 | 4  | 0.955 | 0.960  | 0.953 | 0.960 | 
|  credit-g.arff  | 3 | 20 | 0.701 | 0.743 | 0.723 | 0.754 | 
|  hypothyroid.arff | 9 | 30 | 0.943 | 0.946 | 0.951 | 0.953 |
|  diabetes.arff |  1 | 8 | 0.745 | 0.759 | 0.750 | 0.763 | 

### Perform CFS feature subset selection

| Dataset from WEKA  | selected features | All features   | Precision-selected | Precision-all | recall-selected | Recall-all |
| ------------- |:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|
|  contact-lenses.arff | 2 | 4  | 0.910 | 0.691  | 0.875 | 0.708 | 
|  glass.arff | 5 | 9 | 0.510 | 0.496 | 0.486 | 0.486 |
|  iris.arff | 1 | 5  | 0.955 | 0.960  | 0.953 | 0.960 | 
|  credit-g.arff  | 9 | 21 | 0.715 | 0.743 | 0.733 | 0.754 | 
|  hypothyroid.arff | 8 | 30 | 0.943 | 0.946 | 0.951 | 0.953 |
|  diabetes.arff |  4 | 8 | 0.761 | 0.759 | 0.767 | 0.763 |  
