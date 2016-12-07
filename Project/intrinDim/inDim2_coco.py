#!python
import sys
import hub_toolbox
import numpy as np

from IntrinsicDim import * 
from collections  import defaultdict
from scipy.io     import arff
from Table        import Table, Reader 

table="../data/coc81.arff"

t = Reader( table, ignoreCols=(0,23,24,25,26), sep=" " ).table().oneHot(limit=6)

print( *t.data[:3], sep="\n") 
arr = np.array( t.data ) 
d_mle = intrinsic_dimension( arr, estimator='levina' )
print( d_mle ) 
d_mle = intrinsic_dimension( arr, estimator='mackay' )
print( d_mle ) 

t = Reader( table, ignoreCols=(0,23,25,26), sep=" " ).table().oneHot( limit=6)

print( *t.data[:3], sep="\n") 

arr = np.array( t.data ) 
d_mle = intrinsic_dimension( arr, estimator='levina' )
print( d_mle ) 
d_mle = intrinsic_dimension( arr, estimator='mackay' )
print( d_mle ) 





