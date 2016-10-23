from Table import Reader, Table
from MiniBatch import MiniBatch
from KNN import KNN
from KDTree import KDTree
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
  c_test  = []
  c_train = []
 
 
  for _ in range(5):

    test=tab.sample(x)
    trin=tab.sample(x)

    a = KNN( trin ).test(1, test)
    b = KDTree( trin ).test(test)
    c = MiniBatch( trin, 50, x//10, 10 ).test(test, 1)

    a_train.append( a.train.time ) 
    a_test.append( a.test.time )
    
    b_train.append( b.train.time ) 
    b_test.append( b.test.time )
   
    c_train.append( c.train.time ) 
    c_test.append( c.test.time )
   
  for x,y,z in zip([a,b,c], [a_train, b_train, c_train], [a_test, b_test, c_test]) :
    print ("%15s with %4d rows -> Training Time : %8.4f, Testing Time : %8.4f "%(x.train.algorithm, x.train.size, sorted(y)[2], sorted(z)[2]) )

  
