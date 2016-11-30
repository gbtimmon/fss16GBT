#!python
import sys
import hub_toolbox
import numpy as np

from IntrinsicDim import * 
from collections  import defaultdict
from scipy.io     import arff
from Table        import Table, Reader 

table="../data/cocomosdr.arff"

t = Reader( table, ignoreCols=(0,26), sep="," ).table().oneHot(limit=6)
print( repr(t) ) 
print( *t[1:3], sep="\n" )
arr = np.array( t.data ) 
d_mle = intrinsic_dimension( arr )
print( d_mle ) 

t = Reader( table, ignoreCols=(0,), sep="," ).table().oneHot(limit=6)
print( *t[1:3], sep="\n" )
arr = np.array( t.data ) 
d_mle = intrinsic_dimension( arr )
print( d_mle ) 





