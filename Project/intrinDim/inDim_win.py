#!python
import sys
import hub_toolbox
import numpy as np

from IntrinsicDim import * 
from inDim        import * 
from collections  import defaultdict
from scipy.io     import arff
from Table        import Table, Reader 

table="../data/wine.csv"

k = int( sys.argv[1] ) 
t = Reader( table, ignoreCols=(0,), sep="," ).table()
a = med_id( t, k , k*2 ) 

t = Reader( table, ignoreCols=tuple(), sep="," ).table()
b = med_id( t, k , k*2 ) 

print( list( zip( a, b ) ) ) 





