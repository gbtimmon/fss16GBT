i Homework 4 : KD-Trees and Mini batch K means. 

## Code : 

* [Table](https://github.com/gbtimmon/fss16_teamf/blob/master/Code/4/Table.py) 
* [Mini Batch K Means](https://github.com/gbtimmon/fss16_teamf/blob/master/Code/4/MiniBatchKMeans.py) 
* [KD-Tree](https://github.com/gbtimmon/fss16_teamf/blob/master/Code/4/KDTree.py)
* [KNN](https://github.com/gbtimmon/fss16_teamf/blob/master/Code/4/KNN.py)

## Runtime comparison

Sample runs were run on Diabetes10000.csv from ninja 
Training was performed on 10000 row and training was tested on another 10000 rows. 
Time for loading table is not considered part of training - as a consequence KNN has no training time. 

| Algorithm         | Train Time    | Test Time | Output | 
| ----------------- |:-------------:| ---------:| ------------ |
| KNN               | 0.0 sec | 3877.9398 sec | [output](https://github.com/gbtimmon/fss16_teamf/blob/master/Code/4/KNN.output) |
| Mini Batch KMeans | 175.23852 sec | 3.78731 sec | [output](https://github.com/gbtimmon/fss16_teamf/blob/master/Code/4/MiniBatchKMeans.output) |
| KD-Tree           | 175.23852 sec | 3.78731 sec | [output](https://github.com/gbtimmon/fss16_teamf/blob/master/Code/4/KDTree.output) |


