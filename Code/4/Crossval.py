from __future__ import print_function, division
from O          import o
from KDTree     import KDTree
from KNN        import KNN
from MiniBatch  import MiniBatch
import sys
from Table      import Table, Reader
from math       import floor
from Stats      import rdivDemo

tab            = Reader( sys.argv[1]).table().oneHot(limit=5)
num_of_crosses = int( sys.argv[2] )
increment      = int( len(tab) / num_of_crosses ) 



knr_recall = ["KNN"]
knr_falarm = ["KNN"]
kdr_recall = ["KDTree"]
kdr_falarm = ["KDTree"]
mbr_recall = ["MBatch"]
mbr_falarm = ["MBatch"]
for i in xrange( num_of_crosses ) :

  sys.stdout.flush()

  table_range = lambda k,_ : k >= (increment*i) and k < ( increment*(i+1) )

  test,train = tab.filter( table_range, shallowCopy=True )
 
  kdr = KDTree   ( train ).test(test)
  mbr = MiniBatch( train, 50, 100, 100).test(test, 1)

  print( kdr.info() ) 
  print( mbr.info() ) 

  kdr_recall.append(kdr.metric.recall)
  mbr_recall.append(mbr.metric.recall)
  kdr_falarm.append(kdr.metric.falsealarm)
  mbr_falarm.append(mbr.metric.falsealarm)
 

a1 = [ mbr_recall, kdr_recall ]
a2 = [ mbr_falarm, kdr_falarm ]
rdivDemo( a1 )
rdivDemo( a2 )
