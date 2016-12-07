#!python
import sys
import hub_toolbox
import numpy as np

from IntrinsicDim import * 
from collections  import defaultdict
from scipy.io     import arff
from Table        import Table, Reader 
from Crossval     import crossval

def med_id( t, k1, k2 ) : 
  levina  = []
  mackay  = []

  for table in crossval( t , 10) :
    levina.append( intrinsic_dimension( np.array( table ) , estimator='levina', k1=k1, k2=k2 ) ) 
    mackay.append( intrinsic_dimension( np.array( table ) , estimator='mackay', k1=k1, k2=k2 ) ) 

  return ( np.median( levina ) , np.median( mackay ) ) 




