"""
MiniBatch KMeans

  Input :
    @k     number of clusters
    @b     batch size
    @t     iterations 
    @table table object containing data
  
  Algorithm :
   1.   let C be a set of k randomly picked centers
   2.   v <- 0
   3.   for i in 1 to t :
   4.      M <- b random examples from X
   5.
   6.      for x in M : 
   7.         d[x] <- f(C,x) 
   8.
   9.      for x in M :
  10.         c <- d[x]
  11.         v[c] <- v[c] + 1
  12.         n <- 1/v[c]
  13.         c <- c - nc + cx
  14.       

"""
from __future__ import print_function
from Table import Table, CSVReader
import sys

k   = int(sys.argv[1])
b   = int(sys.argv[2])
t   = int(sys.argv[3])
tab = CSVReader( sys.argv[4] ).table()

# 1
C = tab.sample( k ) 
V = 0
for i in xrange( t ) :
  M = tab.sample( b )
  
  for x in M :
    print ( x ) 
    D = [ tab.closest( c ) for c in C ]
    print (D )



