# Niave Bayes analysis

For this project I compared my KDTree implementation from last week with a new Niave Bayes Classifier 

## Questions  

* The Naive bayes (with roughlt n training time in my implementation, trians faster than the KDTree which has roughly O(n log n ) training time 
* like wise Niave bayes out performs on training times.
* in addition the Niave bayes outperformed KDTree on all three datasets - meaning that faster does not equal worse here. 

## Code 

 * [Niave Bayes](https://github.com/gbtimmon/fss16_teamf/tree/master/Code/5/NB.py)
 * [KDTree](https://github.com/gbtimmon/fss16_teamf/tree/master/Code/5/KDTree.py)
 * [Table](https://github.com/gbtimmon/fss16_teamf/tree/master/Code/5/Table.py)

## Datasets 

### [Diabetes 10000](https://github.com/dotninjas/dotninjas.github.io/blob/master/ninja/data/diabetes10000.csv):
As the orginal file contains duplicates, it has been deduped down to an original ~800 rows. This prevents unnatrually good results in knn style classification (which would just reutrn itself).

~800 rows, 9 inputs, 2 output classes. 

### [Mnist images1](https://github.com/gbtimmon/fss16_teamf/tree/master/Code/5/mnist_pca_labled.csv):
This data is generated from the famous MNIST data set. Available [here](http://yann.lecun.com/exdb/mnist/). The data was preprocesses using a basic pca feature reduction down to the 10 most significant features. Data set 1 contains 60000 records but images are labeled simple "seven" or "not seven" to aid in classification metric measurement

60000 rows, 10 inputs, 2 output classes. 

### [Mninst images2](https://github.com/gbtimmon/fss16_teamf/tree/master/Code/5/mnist_pca_8or9.csv):
This is data similar to the one above but only example of the 8 and 9 digit were extracted. Preprocess was the same. 


~12000 rows, 10 inputs, 2 output classes. 

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

## Samples outputs:

### KDTree output : 

    Training :
        set             : Table(12524)
        time            : 0.134001417963
        algorithm       : KDTree
        size            : 692
   
    Testing :
        set             : Table(12522)
        time            : 0.025937031721
        size            : 76
   
    Results Summary :
   
           ID |                     Value |  Exp Count |  Prd Count
        ----- + ------------------------- + ---------- + ----------
            1 |      ('tested_positive',) |         49 |         30
            2 |      ('tested_negative',) |         27 |         46
    
        Confusion Matrix
                *Using Minority Class as Positive: ('tested_negative',)
   
              | Exp T | Exp F
        ----- + ----- + -----
        Prd T |    18 |    28
        Prd F |     9 |    21
   
    Metrics
        f1          = 0.493
        recall      = 0.667
        falsealarm  = 0.571
        precision   = 0.391
        specificity = 0.429
        accuracy    = 0.513

### MiniBatch Output :

    Training :
        set             : Table(1)
        algorithm       : MiniBatch
        batchSize       : 100
        iterCount       : 100
        time            : 1.57839770221
        clusterCnt      : 5
        size            : 768
    
    Testing :
        knn             : 1
        set             : Table(2)
        time            : 101.96071075
        size            : 768
    
    Results Summary :
    
           ID |                     Value |  Exp Count |  Prd Count
        ----- + ------------------------- + ---------- + ----------
            2 |      ('tested_positive',) |        268 |        242
            1 |      ('tested_negative',) |        500 |        526
    
        Confusion Matrix
                *Using Minority Class as Positive: ('tested_positive',)
    
              | Exp T | Exp F
        ----- + ----- + -----
        Prd T |   121 |   121
        Prd F |   147 |   379
    
    Metrics
        f1          = 0.475
        recall      = 0.451
        falsealarm  = 0.242
        precision   = 0.500
        specificity = 0.758
        accuracy    = 0.651
  

## Performance (diabetes deduped ) : 

10 way cross validation was used to produce all of the performance distributions below.

### Recall

    rank ,         name ,    med   ,  iqr
    ----------------------------------------------------
       1 ,       MBatch ,    0.35  ,  0.09 (  -- *  -------|------------- ), 0.30,  0.35,  0.38,  0.43,  0.89
       1 ,       KDTree ,    0.48  ,  0.11 (    ----  *  --|---           ), 0.35,  0.43,  0.48,  0.54,  0.67
    
### False Alarm

    rank ,         name ,    med   ,  iqr
    ----------------------------------------------------
       1 ,       KDTree ,    0.24  ,  0.15 (  --      *----|-----         ), 0.15,  0.21,  0.32,  0.35,  0.57
       1 ,       MBatch ,    0.37  ,  0.09 (        --  *--|------------- ), 0.29,  0.32,  0.37,  0.40,  0.76


## Performance (MNIST Images 1):

### Recall

    rank ,         name ,    med   ,  iqr
    ----------------------------------------------------
       1 ,       MBatch ,    0.48  ,  0.33 (      --       |    *  -      ), 0.31,  0.35,  0.60,  0.67,  0.68
       2 ,       KDTree ,    0.69  ,   0.1 (               |    -    *--- ), 0.61,  0.64,  0.71,  0.73,  0.81

### False Alarm

    rank ,         name ,    med   ,  iqr
    ----------------------------------------------------
       1 ,       KDTree ,    0.04  ,  0.02 (   --  *   --- |              ), 0.03,  0.03,  0.04,  0.05,  0.06
       2 ,       MBatch ,    0.07  ,  0.02 (         ----- |  *           ), 0.05,  0.06,  0.07,  0.11,  0.11
    
## Performance (MNIST Images 2 ) :

### Recall

    rank ,         name ,    med   ,  iqr
    ----------------------------------------------------
       1 ,       MBatch ,    0.83  ,  0.09 (           --  |  *    ---    ), 0.77,  0.79,  0.83,  0.87,  0.90
       1 ,       KDTree ,    0.87  ,  0.08 (              -|---     * --- ), 0.80,  0.84,  0.88,  0.90,  0.93

### False Alarm

    rank ,         name ,    med   ,  iqr
    ----------------------------------------------------
       1 ,       KDTree ,     0.1  ,  0.05 (      ---   *  |     --       ), 0.07,  0.09,  0.11,  0.16,  0.17
       1 ,       MBatch ,     0.1  ,  0.11 (  -            | *   -------- ), 0.05,  0.05,  0.13,  0.16,  0.20



    
    
