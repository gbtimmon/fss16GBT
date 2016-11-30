import sys
import numpy as np
import sklearn as sk

from scipy.io import arff
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB



if __name__ == '__main__' : 
  data, meta = arff.loadarff( open( 'nasa93.arff' ) ) 
  data = np.array([ list(x) for x in data ], dtype=(np.str_) )
  print( meta ) 
  iv =  data[:, [ 5,6,7,8,11,12,13,14,15,17,18,19,20,22]] 
  dv =  data[:, 23 ]

  gnb = GaussianNB()
  y_pred = gnb.fit( iv, dv ).predict( iv ) 

  print( y_pred )