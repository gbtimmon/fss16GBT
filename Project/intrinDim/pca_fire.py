#!python
import sys
import numpy as np

from collections  import defaultdict
from pca import *
from scipy.io     import arff
from Table        import Table, Reader 
from inDim        import *

table="../data/forestfire.csv"

t = Reader( table, ignoreCols=(2,3,12), sep="," ).table()
pca( t, 0.030 ) 
pca( t, 0.020 ) 
pca( t, 0.010 ) 
t = Reader( table, ignoreCols=(2,3), sep="," ).table()

pca( t, 0.030 ) 
pca( t, 0.020 ) 
pca( t, 0.010 ) 





