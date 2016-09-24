"""
MiniBatch KMeans

  Input :
    @k     number of clusters
    @b     batch size
    @t     iterations 
    @table table object containing data
  
  Algorithm :
   0.   let C be a set of k randomly picked centers
   1.   v <- 0
   2.   for i in 1 to t :
   3.      M <- b random examples from X
   4.      for x in M : d[x] <- f(C,x) 
   5.      for x in M :
   6.         c <- d[x]
   7.         v[c] <- v[c] + 1
   8.         n <- 1/v[c]
   9.         c <- c - nc + cx

"""
from __future__ import division
from Table import Table, CSVReader
from math import floor
import sys

class Unbuffered(object):
  def __init__(self, stream):
    self.stream = stream
  def write(self, data):
    self.stream.write(data)
    self.stream.flush()
  def __getattr__(self, attr):
    return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

k   = int(sys.argv[1])
b   = int(sys.argv[2])
t   = int(sys.argv[3])
tab = CSVReader( sys.argv[4] ).table()

C  = tab.sample( k, shallowCopy=False ) # 0. initial random centers
V = [0] * len(C)                        # 1. size of the current cluster
print("Start")
for i in xrange( t ) :                  # 2. for all iters
  p = int(i/t * 100)
  print "\r[" + ( "#" * p ) + ("-" * (100-p)) + "]", 
  M = tab.sample( b )                   # 3. random samples from data set  
  D = [ C.closesti( k ) for k in M ]    # 4. closest center of each sample
  for x,c in zip(M,D) :                 # 5,6. for each sample and closest center
    if isinstance( c, list) : c = c[0]  # if I got more than one center
    V[c] += 1                           # 7. grow the center
    C.blendRow(c, x, 1/V[c] )           # 8,9. blend the center
    

print("\r Complete")
print()
print (C)
print()
print (C.dataStr())
    




