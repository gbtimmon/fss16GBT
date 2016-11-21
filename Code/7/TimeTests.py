from Table import Reader, Table
from KDTree import KDTree
from NB import NB
from O import o 
import sys


tab = Reader(sys.argv[1]).table()

data = o()

sz = [250, 500, 1000, 2000 ]
for x in sz :
  a_test  = []
  a_train = []
  b_test  = []
  b_train = []
 
 
  for _ in range(5):

    test=tab.sample(x)
    trin=tab.sample(x)

    a = NB( trin ).test(test)
    b = KDTree( trin ).test(test)

    a_train.append( a.train.time ) 
    a_test.append( a.test.time )
    
    b_train.append( b.train.time ) 
    b_test.append( b.test.time )
   
   
  for x,y,z in zip([a,b], [a_train, b_train], [a_test, b_test]) :
    print ("%15s with %4d rows -> Training Time : %8.4f, Testing Time : %8.4f "%(x.train.algorithm, x.train.size, sorted(y)[2], sorted(z)[2]) )

  
