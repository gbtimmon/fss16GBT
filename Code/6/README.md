# Generator : 

Generator code is available [Here](https://github.com/gbtimmon/fss16_teamf/tree/master/Code/6/Generator.py)

The generator has three main functions : 
 
    def __init__( table ) : #Sets the initial data to read from. Dynamically sets number of classes 
    def setProb( tuple )  : #passes in a vector of each class probability. 
    def getRow()          : #Pulls a random row without replacement from the table by the probabilities passed in

# DataReader : 

Data was passed to an incremental Niave Bayes Classifier. Incremental Niave Bayes Code is here [Here](https://github.com/gbtimmon/fss16_teamf/tree/master/Code/6/IncrementalNB.py)
A testing sciprt available here passed rows from the Generator to the Incremental Niave Bayes 100 rows at a time and recall was reported. Reported values are media of five runs.
The Niave Bayes was seed with 100 random initial rows with probability 

    Era  1 : Recall = 0.94, Probability = ( 50, 50,  0 )
    Era  2 : Recall = 0.91, Probability = ( 50, 50,  0 )
    Era  3 : Recall = 0.96, Probability = ( 50, 50,  0 )
    Era  4 : Recall = 0.97, Probability = ( 50, 50,  0 )
    Era  5 : Recall = 0.94, Probability = ( 50, 50,  0 )
    Era  6 : Recall = 0.99, Probability = ( 50, 50,  0 )
    Era  7 : Recall = 0.95, Probability = ( 50, 50,  0 )
    Era  8 : Recall = 0.95, Probability = ( 50, 50,  0 )
    Era  9 : Recall = 0.86, Probability = ( 50, 50,  0 )
    Era 10 : Recall = 0.93, Probability = ( 50, 50,  0 )
    Era 11 : Recall = **0.66**, Probability = ( 10, 30, 60 )
    Era 12 : Recall = 0.96, Probability = ( 10, 30, 60 )
    Era 13 : Recall = 0.82, Probability = ( 10, 30, 60 )
    Era 14 : Recall = 0.93, Probability = ( 10, 30, 60 )
    Era 15 : Recall = 0.96, Probability = ( 10, 30, 60 )
    Era 16 : Recall = 0.97, Probability = ( 10, 30, 60 )
    Era 17 : Recall = 0.92, Probability = ( 10, 30, 60 )
    Era 18 : Recall = 0.96, Probability = ( 10, 30, 60 )
    Era 19 : Recall = 0.92, Probability = ( 10, 30, 60 )
    Era 20 : Recall = 0.98, Probability = ( 10, 30, 60 )
    
# Incremental NB

The Incremental NB was adjusted to output the predicted class a log-likely hood of those prediction

    ...
    Era  6 : Recall = 0.94, Probability = ( 50, 50,  0 )
           0_value median log-likelihood is -73.08
           6_value median log-likelihood is -71.54
    Era  7 : Recall = 0.92, Probability = ( 50, 50,  0 )
           0_value median log-likelihood is -73.21
           6_value median log-likelihood is -71.64
    Era  8 : Recall = 0.93, Probability = ( 50, 50,  0 )
           0_value median log-likelihood is -73.06
           6_value median log-likelihood is -71.72
    Era  9 : Recall = 0.96, Probability = ( 50, 50,  0 )
           0_value median log-likelihood is -72.70
           6_value median log-likelihood is -71.98
    Era 10 : Recall = 0.98, Probability = ( 50, 50,  0 )
           0_value median log-likelihood is -73.37
           6_value median log-likelihood is -71.83
    Era 11 : Recall = **0.64**, Probability = ( 10, 30, 60 )
           0_value median log-likelihood is **-74.67**
           6_value median log-likelihood is **-75.33**
    Era 12 : Recall = 0.96, Probability = ( 10, 30, 60 )
           1_value median log-likelihood is -69.22
           0_value median log-likelihood is -72.53
           6_value median log-likelihood is -70.97
    Era 13 : Recall = 0.98, Probability = ( 10, 30, 60 )
           1_value median log-likelihood is -68.32
           0_value median log-likelihood is -73.51
           6_value median log-likelihood is -70.90
    ...

#Anamoly Detector : 

With the log likely hood of each set kept in a distribution, the distributions were compared with the A12 test and this was used to create an anomaly detector 
    
    Era 1 : anomaly detected False
    Era 2 : anomaly detected False
    Era 3 : anomaly detected False
    Era 4 : anomaly detected False
    Era 5 : anomaly detected False
    Era 6 : anomaly detected False
    Era 7 : anomaly detected False
    Era 8 : anomaly detected False
    Era 9 : anomaly detected False
    Era 10 : anomaly detected False
    Era 11 : anomaly detected **True**
    Era 12 : anomaly detected False
    Era 13 : anomaly detected False
    Era 14 : anomaly detected False
    Era 15 : anomaly detected False
    Era 16 : anomaly detected False
    Era 17 : anomaly detected False
    Era 18 : anomaly detected False
    Era 19 : anomaly detected False
    Era 20 : anomaly detected False
    
