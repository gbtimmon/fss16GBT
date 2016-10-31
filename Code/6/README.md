# Generator : 

Generator code is available [Here](https://github.com/gbtimmon/fss16_teamf/tree/master/Code/6/Generator.py)

The generator has three main functions : 
 
    def __init__( table ) : #Sets the initial data to read from. Dynamically sets number of classes 
    def setProb( tuple )  : #passes in a vector of each class probability. 
    def getRow()          : #Pulls a random row without replacement from the table by the probabilities passed in

# DataReader : 

Data was passed to an incremental Niave Bayes Classifier. Incremental Niave Bayes Code is here [Here](https://github.com/gbtimmon/fss16_teamf/tree/master/Code/6/IncrementalNB.py)
A testing sciprt available here passed rows from the Generator to the Incremental Niave Bayes 100 rows at a time and recall was reported. Reported values are media of five runs.


