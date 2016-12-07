#!python
import sys
import hub_toolbox
import numpy as np

from IntrinsicDim import * 
from collections  import defaultdict
from scipy.io     import arff
from Table        import Table, Reader 
from inDim        import *

table="../data/forestfire.csv"

k = int(sys.argv[1])
t = Reader( table, ignoreCols=(2,3,12), sep="," ).table()
a = med_id(t, k , 2*k)
t = Reader( table, ignoreCols=(2,3), sep="," ).table()
b = med_id(t, k, 2*k)
print( list(zip(a,b)))






