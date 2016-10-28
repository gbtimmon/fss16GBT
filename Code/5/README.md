### Niave Bayes analysis

For this project I compared my KDTree implementation from last week with a new Niave Bayes Classifier 

## Code 

 * [Niave Bayes](https://github.com/gbtimmon/fss16_teamf/tree/master/Code/5/NB.py)
 * [KDTree](https://github.com/gbtimmon/fss16_teamf/tree/master/Code/5/KDTree.py)
 * [Table](https://github.com/gbtimmon/fss16_teamf/tree/master/Code/5/Table.py)

## Datasets 

 * [Diabetes 1000](https://github.com/dotninjas/dotninjas.github.io/blob/master/ninja/data/diabetes10000.csv) : 10000 rows, 8 independent attribute, 1 dependent attribute
 * [JEdit](https://github.com/gbtimmon/fss16_teamf/blob/master/Code/4/jedit.csv) 365 rows, 20 independent attributes, 1 dependent attribute

## Time analysis 

 Times were tested with the script [TimeTests.py](https://github.com/gbtimmon/fss16_teamf/blob/master/Code/5/TimeTests.py)
 
  
    
    Niave Bayes with  250 rows -> Training Time :  -0.0045, Testing Time :  -0.0053 
         KDTree with  250 rows -> Training Time :   0.0398, Testing Time :   0.0689 
    Niave Bayes with  500 rows -> Training Time :  -0.0116, Testing Time :  -0.0133 
         KDTree with  500 rows -> Training Time :   0.1245, Testing Time :   0.2255 
    Niave Bayes with 1000 rows -> Training Time :  -0.0245, Testing Time :  -0.0262 
         KDTree with 1000 rows -> Training Time :   0.2898, Testing Time :   0.5398 
    Niave Bayes with 2000 rows -> Training Time :  -0.0470, Testing Time :  -0.0521 
         KDTree with 2000 rows -> Training Time :   0.6142, Testing Time :   1.2398 
