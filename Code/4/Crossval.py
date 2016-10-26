from __future__ import print_function, division
from O import o
from KDTree import KDTree
from MiniBatch import MiniBatch
import sys
from Table import Table, Reader
from math import floor

tab            = Reader( sys.argv[1]).table().sample(1000).oneHot()

num_of_crosses = int( sys.argv[2] )
increment      = int( len(tab) / num_of_crosses ) 


metrics = o()
metrics.kdtree = o()
metrics.kdtree.tpr = []
metrics.kdtree.fdr = []
metrics.mbatch = o()
metrics.mbatch.tpr = []
metrics.mbatch.fdr = []

for i in xrange( num_of_crosses ) :
 
  table_range = lambda k,_ : k >= (increment*i) and k < ( increment*(i+1) )

  test,train = tab.filter( table_range, shallowCopy=True )
 
  kdr = KDTree   ( train ).test(test)
  mbr = MiniBatch( train, 10, 10, 10 ).test(test, 1)

  metrics.kdtree.tpr.append( kdr.metric.tpr )
  metrics.kdtree.fdr.append( kdr.metric.fdr )
  metrics.mbatch.tpr.append( mbr.metric.tpr )
  metrics.mbatch.fdr.append( mbr.metric.fdr )


print( sorted( metrics.kdtree.tpr ) )
print( sorted( metrics.kdtree.fdr ) )
print( sorted( metrics.mbatch.tpr ) )
print( sorted( metrics.mbatch.fdr ) )
