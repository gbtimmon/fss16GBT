#!python
import sys
import hub_toolbox
import numpy as np

from IntrinsicDim import * 
from collections  import defaultdict
from scipy.io     import arff
from Table        import Table, Reader 

table="../data/mnist_pca_8or9.csv"

t = Reader( table, ignoreCols=(10,), sep="," ).table()
print( *t[1:3], sep="\n" )
arr = np.array( t.data ) 
d_mle = intrinsic_dimension( arr )
print( d_mle ) 

t = Reader( table, ignoreCols=tuple(), sep="," ).table()

t.header[10].dep = False

t = t.oneHot() 
print( *t[1:3], sep="\n" )
arr = np.array( t.data ) 
d_mle = intrinsic_dimension( arr )
print( d_mle ) 





