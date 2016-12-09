#!python
import sys
import numpy as np

from IntrinsicDim import * 
from inDim        import * 
from collections  import defaultdict
from scipy.io     import arff
from Table        import Table, Reader 
from inDim        import *

table="../data/iris.csv"

k = int( sys.argv[1] ) 

t = Reader( table, ignoreCols=(3,4,5), sep="," ).table().oneHot()

a = med_id(t,k,2*k)

t = Reader( table, ignoreCols=tuple(), sep="," ).table().oneHot()
b= med_id(t,k,2*k) 

print( a, b ) 






