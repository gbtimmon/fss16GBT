#!python
import sys
import numpy as np

from pca import *
from collections  import defaultdict
from scipy.io     import arff
from Table        import Table, Reader 
from inDim import *

table="../data/maxwell.arff"

t = Reader( table, ignoreCols=(0,24,25,26), sep="," ).table()
pca( t, 0.03 ) 
pca( t, 0.02 ) 
pca( t, 0.01, plot = True ) 


t = Reader( table, ignoreCols=(0,), sep="," ).table()
pca( t, 0.03 ) 
pca( t, 0.02 ) 
pca( t, 0.01, plot = True ) 






