#!python
import sys
import numpy as np

from IntrinsicDim import * 
from inDim        import *
from collections  import defaultdict
from scipy.io     import arff
from Table        import Table, Reader 

table="../data/mnist_pca_8or9.csv"

k = int( sys.argv[1] )

t = Reader( table, ignoreCols=(10,), sep="," ).table().sample(100)
a = med_id( t, k, k*2 ) 

t = Reader( table, ignoreCols=tuple(), sep="," ).table().sample(100)
t.header[10].dep = False
t = t.oneHot() 
b = med_id( t, k , k*2  ) 


print( a, b ) 







