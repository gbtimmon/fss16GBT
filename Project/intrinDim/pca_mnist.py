#!python
import sys
import numpy as np

from collections  import defaultdict
from pca import *
from scipy.io     import arff
from Table        import Table, Reader 

table="../data/mnist_pca_8or9.csv"
t = Reader( table, ignoreCols=(10,), sep="," ).table().sample(100)
pca( t, 0.03 )
pca( t, 0.02 )
pca( t, 0.01, plot=True )

t = Reader( table, ignoreCols=tuple(), sep="," ).table().sample(100)
t.header[10].dep = False
t = t.oneHot() 
pca( t, 0.03 )
pca( t, 0.02 )
pca( t, 0.01, plot=True )







