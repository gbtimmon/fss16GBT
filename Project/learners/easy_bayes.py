import sys
import numpy as np
import sklearn as sk

from scipy.io import arff
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from Table import Reader, Table 



if __name__ == '__main__' : 


  t = Reader( "../data/nasa93.arff", sep=",").table()

  print( *t[1:3] ) 

  
