#!python
import sys
import numpy as np

from IntrinsicDim import * 
from collections  import defaultdict
from scipy.io     import arff
from Table        import Table, Reader 
from inDim import *

table="../data/maxwell.arff"

k = int( sys.argv[1] ) 
t = Reader( table, ignoreCols=(0,24,25,26), sep="," ).table()
a = med_id( t, k, k*2 ) 


t = Reader( table, ignoreCols=(0,), sep="," ).table()
b = med_id(t, k, k* 2) 

print( a,b ) 





