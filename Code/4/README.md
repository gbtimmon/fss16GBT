i Homework 4 : KD-Trees and Mini batch K means. 

## Code : 

* [Table](https://github.com/gbtimmon/fss16_teamf/blob/master/Code/4/Table.py) 
* [Mini Batch K Means](https://github.com/gbtimmon/fss16_teamf/blob/master/Code/4/MiniBatchKMeans.py) 
* [KD-Tree](https://github.com/gbtimmon/fss16_teamf/blob/master/Code/4/KDTree.py)
* [KNN](https://github.com/gbtimmon/fss16_teamf/blob/master/Code/4/KNN.py)

## Runtime comparison

Samples runs were run on diabetes100000.csv from the ninja datasets. 
A random sample fo the specified size was takes for each test. 
Each test is run 5 times and the median result was reported below. 
Sets of size 250, 500, 1000 and 2000 were tested. 

With 250 rows :
            KNN -> Training Time :   0.0000, Testing Time :   1.8238
         KDTree -> Training Time :   0.0518, Testing Time :   0.0838
      MiniBatch -> Training Time :   0.3707, Testing Time :   0.3577

With 500 rows : 
            KNN -> Training Time :   0.0000, Testing Time :   7.6799
         KDTree -> Training Time :   0.1333, Testing Time :   0.2168
      MiniBatch -> Training Time :   0.8090, Testing Time :   0.7939

With 1000 rows :
            KNN -> Training Time :   0.0000, Testing Time :  32.5580
         KDTree -> Training Time :   0.3100, Testing Time :   0.5443
      MiniBatch -> Training Time :   1.6013, Testing Time :   1.5249

With 2000 rows : 
            KNN -> Training Time :   0.0000, Testing Time : 156.3769
         KDTree -> Training Time :   0.8651, Testing Time :   1.7281
      MiniBatch -> Training Time :   4.2436, Testing Time :   4.1740


