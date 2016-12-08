#!python
import sys
import numpy as np

from collections  import defaultdict
from pca import *
from scipy.io     import arff
from Table        import Table, Reader 
from inDim        import *

table="../data/iris.csv"


t = Reader( table, ignoreCols=(3,4,5), sep="," ).table().oneHot()
pca( t, 0.03)
pca( t, 0.02)
pca( t, 0.01, plot=True) 


t = Reader( table, ignoreCols=tuple(), sep="," ).table().oneHot()
pca( t, 0.03)
pca( t, 0.02)
pca( t, 0.01, plot=True) 






