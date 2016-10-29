### Niave Bayes analysis

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

# [Diabetes 10000](https://github.com/dotninjas/dotninjas.github.io/blob/master/ninja/data/diabetes10000.csv):
As the orginal file contains duplicates, it has been deduped down to an original ~800 rows. This prevents unnatrually good results in knn style classification (which would just reutrn itself).

~800 rows, 9 inputs, 2 output classes. 

# [Mnist images1](https://github.com/gbtimmon/fss16_teamf/tree/master/Code/5/mnist_pca_labled.csv):
This data is generated from the famous MNIST data set. Available [here](http://yann.lecun.com/exdb/mnist/). The data was preprocesses using a basic pca feature reduction down to the 10 most significant features. Data set 1 contains 60000 records but images are labeled simple "seven" or "not seven" to aid in classification metric measurement

60000 rows, 10 inputs, 2 output classes. 

# [Mninst images2](https://github.com/gbtimmon/fss16_teamf/tree/master/Code/5/mnist_pca_8or9.csv):
This is data similar to the one above but only example of the 8 and 9 digit were extracted. Preprocess was the same. 


60000 rows, 10 inputs, 2 output classes. 


## Time analysis 

 Times were tested with the script [TimeTests.py](https://github.com/gbtimmon/fss16_teamf/blob/master/Code/5/TimeTests.py)
 
#  train and test 250 rows
    Niave Bayes -> Training Time:   0.0045, Testing Time:   0.0053
         KDTree -> Training Time:   0.0398, Testing Time:   0.0689
#  train and test 500 rows
    Niave Bayes -> Training Time:   0.0116, Testing Time:   0.0133
         KDTree -> Training Time:   0.1245, Testing Time:   0.2255
#  train and test 1000 rows
    Niave Bayes -> Training Time:   0.0245, Testing Time:   0.0262
         KDTree -> Training Time:   0.2898, Testing Time:   0.5398
#  train and test 2000 rows
    Niave Bayes -> Training Time:   0.0470, Testing Time:   0.0521
         KDTree -> Training Time:   0.6142, Testing Time:   1.2398

## Samples outputs:

# KDTree output : 
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

# Niave Bayes Output :

   Training :
       set             : Table(12523)
       algorithm       : Niave Bayes
       time            : 0.0266010108905
       pdf             : gauss
       size            : 692
   
   Testing :
       size            : 76
       set             : Table(12522)
       time            : 0.00269815554324
   
   Results Summary :
   
          ID |                     Value |  Exp Count |  Prd Count
       ----- + ------------------------- + ---------- + ----------
           1 |      ('tested_positive',) |         49 |         48
           2 |      ('tested_negative',) |         27 |         28
   
       Confusion Matrix
               *Using Minority Class as Positive: ('tested_negative',)
   
             | Exp T | Exp F
       ----- + ----- + -----
       Prd T |    18 |    10
       Prd F |     9 |    39
   
   Metrics
       f1          = 0.655
       recall      = 0.667
       falsealarm  = 0.204
       precision   = 0.643
       specificity = 0.796
       accuracy    = 0.750
   

## Performance (diabetes deduped ) : 

10 way cross validation was used to produce all of the performance distributions below.

#Recall

    rank ,         name ,    med   ,  iqr
    ----------------------------------------------------
       1 ,       KDTree ,    0.48  ,  0.11 (     ----  * --|---           ), 0.35,  0.43,  0.48,  0.54,  0.67
       1 ,           NB ,    0.52  ,  0.22 (         -   * |   ---------- ), 0.43,  0.47,  0.54,  0.67,  0.90
    
#False Alarm

    rank ,         name ,    med   ,  iqr
    ----------------------------------------------------
       1 ,           NB ,    0.11  ,  0.05 (-- *    -------|-----------   ), 0.08,  0.10,  0.12,  0.20,  0.53
       1 ,       KDTree ,    0.24  ,  0.15 (    ----       * ------------ ), 0.15,  0.21,  0.32,  0.35,  0.57

## Performance (MNIST Images 1):

#Recall

    rank ,         name ,    med   ,  iqr
    ----------------------------------------------------
       1 ,       KDTree ,    0.69  ,   0.1 (   ----        |* ----------- ), 0.61,  0.64,  0.71,  0.73,  0.81
       1 ,           NB ,    0.71  ,  0.02 (               | *-----       ), 0.70,  0.71,  0.71,  0.73,  0.76
    
#False Alarm

    rank ,         name ,    med   ,  iqr
    ----------------------------------------------------
       1 ,           NB ,    0.01  ,   0.0 ( *-            |              ), 0.01,  0.01,  0.01,  0.01,  0.01
       2 ,       KDTree ,    0.04  ,  0.02 (         ----  |*       ----- ), 0.03,  0.03,  0.04,  0.05,  0.06
    
## Performance (MNIST Images 2 ) :

#Recall

    rank ,         name ,    med   ,  iqr
    ----------------------------------------------------
       1 ,       KDTree ,    0.87  ,  0.08 ( -------       |*   -----     ), 0.80,  0.84,  0.88,  0.90,  0.93
       2 ,           NB ,    0.93  ,  0.02 (               |       -- *-- ), 0.92,  0.93,  0.94,  0.94,  0.95

#False Alarm
    
    rank ,         name ,    med   ,  iqr
    ----------------------------------------------------
       1 ,           NB ,    0.05  ,  0.01 (-    * --      |              ), 0.04,  0.05,  0.06,  0.07,  0.08
       2 ,       KDTree ,     0.1  ,  0.05 (      -----    *           -- ), 0.07,  0.09,  0.11,  0.16,  0.17
    
