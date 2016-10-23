from __future__   import division, print_function
from Table        import Table, Reader
from O            import o 
from math         import floor
from time         import clock
from ResultSet    import ResultSet
import sys

__DOC__=(
"""
MiniBatch KMeans
  Author : Greg Timmons
  Date   : Fall 2016

  Input :
    @1     nCLusters : number of clusters
    @2     bSize     : batch size
    @3     iters     : iterations 
    @4     kNN       : nearest neighbors to search
    @5     trainSet  : training set
    @6     testSet   : testing set

    @      log       : output stream to write info message (allows you to redirect to a file)
                       default : sys.stdout
  
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
)

class MiniBatch(o) :
  def __init__(self, trainSet, nClusters, bSize, iters ):
    super(MiniBatch, self).__init__()
    self.algorithm  = "MiniBatch"
    self.clusterCnt = k = int(nClusters)
    self.batchSize  = b = int(bSize)
    self.iterCount  = t = int(iters)

    if not isinstance( trainSet, Table ) :  
      trainSet = Reader( trainSet ).table()
      
    self.set = trainSet
    self.size = len(trainSet)

        
    t0 = clock() #python on windows needs to use clock, 
               #since the system clock is different. 
               #clock on *nix seems to work fine, so clock seems to be
               # more portable in general. 

    self._C = self.set.sample( k, shallowCopy=False )# 0. initial random centers
    V = [0] * len(self._C)                         # 1. size of the current cluster
    for i in xrange( t ) :                      # 2. for all iters
      p = int(i/t * 50) + 1                     # _. show the percent complete. 
      M = self.set.sample( b )                       # 3. random samples from data set  
      D = [ self._C.closesti( k ) for k in M ]  # 4. closest center of each sample
    
      for x,c in zip(M,D) :                     # 5,6. for each sample and closest center
        if isinstance( c, list) : c = c[0]      # if I got more than one center
        c=c[0]
        V[c] += 1                               # 7. grow the center
        self._C.blendRow(c, x, 1/V[c] )         # 8,9. blend the center

    t1 = clock()

    self.time = t1 - t0

  def test(self, testSet, k ):
    
    if not isinstance( testSet, Table ) :
      testSet = Reader( testSet ).table()

    t0 = clock()
    rslt = [ ( x, self._C.closest(x) ) for x in testSet ]
    t1 = clock() 

    testObj = o()
    testObj.set  = testSet
    testObj.size = len( testSet ) 
    testObj.time = t1 - t0
    testObj.knn      = k
   
    return ResultSet( self, testObj, rslt )
 
  
if __name__ == '__main__' : 
  try : 
    k   = int( sys.argv[1] )       
    b   = int( sys.argv[2] )       
    t   = int( sys.argv[3] )       
    knn = int( sys.argv[4] )       
    trn = sys.argv[5]       
    tst = sys.argv[6] 
  except : 
    sys.stderr.write( cstr(" Illegal Arguments\n greater than", "r") )
    sys.stderr.write( __DOC__ )
    exit(1)

  trn = Reader( trn ).table().sample(100)
  tst = Reader( tst ).table().sample(100)

  mt = MiniBatchKNN( trn, k, b, t )
  rs = mt.test( tst, knn )

  print(rs)
  print(rs.info())

      
  
  
  
