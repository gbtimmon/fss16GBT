#!python
import sys
import numpy as np

from IntrinsicDim import * 
from collections  import defaultdict
from scipy.io     import arff
from Table        import Table, Reader 
from Crossval     import crossval

def med_id( t, k1, k2 ) : 
  levina  = []
  for table in crossval( t , 10) :
    levina.append( intrinsic_dimension( np.array( table ) , estimator='levina', kmin=k1, kmax=k2 ) ) 

  return ( np.median( levina )) 





