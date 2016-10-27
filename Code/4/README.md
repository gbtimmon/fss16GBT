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

## Sample Outout from KDTree and MiniBatch K Means `

# KDTree

    Training :
        set             : Table(162221)
        time            : 3.46127011873
        algorithm       : KDTree
        size            : 9000
    
    Testing :
        set             : Table(162219)
        time            : 0.872684954911
        size            : 999
    
    Results Summary :
    
           ID |                     Value |  Exp Count |  Prd Count
        ----- + ------------------------- + ---------- + ----------
            2 |      ('tested_positive',) |        346 |        349
            1 |      ('tested_negative',) |        653 |        650
    
        Confusion Matrix
                *Using Minority Class as Positive: ('tested_positive',)
    
              | Exp T | Exp F
        ----- + ----- + -----
        Prd T |   345 |     4
        Prd F |     1 |   649
    
    Metrics    
        f1          = 0.993
        recall      = 0.997
        falsealarm  = 0.006
        precision   = 0.989
        specificity = 0.994
        accuracy    = 0.995

# MiniBatch

    Training :
        set             : Table(162220)
        algorithm       : MiniBatch
        batchSize       : 500
        iterCount       : 20
        time            : 28.887434214
        clusterCnt      : 100
        size            : 9000
    
    Testing :
        knn             : 1
        set             : Table(162219)
        time            : 2.81676109224
        size            : 999
    
    Results Summary :
    
           ID |                     Value |  Exp Count |  Prd Count
        ----- + ------------------------- + ---------- + ----------
            2 |      ('tested_positive',) |        346 |        272
            1 |      ('tested_negative',) |        653 |        727
    
        Confusion Matrix
                *Using Minority Class as Positive: ('tested_positive',)
    
              | Exp T | Exp F
        ----- + ----- + -----
        Prd T |   103 |   169
        Prd F |   243 |   484
    
    Metrics 
        f1          = 0.333
        recall      = 0.298
        falsealarm  = 0.259
        precision   = 0.379
        specificity = 0.741
        accuracy    = 0.588

##Scott Knott Analysis of diabetes10000.csv cross validated 10 ways : 

# Recall

    rank ,         name ,    med   ,  iqr
    ----------------------------------------------------
       1 ,       MBatch ,     0.4  ,  0.05 ( ----*   -     |              ), 0.30,  0.38,  0.41,  0.49,  0.52
       2 ,       KDTree ,     1.0  ,   0.0 (               |             *), 1.00,  1.00,  1.00,  1.00,  1.00

# False Alarm
    
    rank ,         name ,    med   ,  iqr
    ----------------------------------------------------
       1 ,       KDTree ,     0.0  ,  0.01 (*              |              ), 0.00,  0.00,  0.00,  0.01,  0.02
       2 ,       MBatch ,    0.33  ,  0.04 (               |   -----*---- ), 0.26,  0.33,  0.33,  0.34,  0.41
    
