from __future__  import division, print_function
from Table       import Table, Reader
from XStream     import XStream, cstr
from math        import floor
from time        import clock
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

def MiniBatchKNN( nClusters, bSize, iters, kNN, trainSet, testSet, log=sys.stdout ) :

  #Cusomize the output streams
  out = XStream( sys.stdout, auto_flush=True, color="w" )
  err = XStream( sys.stderr, auto_flush=True, color="r" )
  
  k   = int(nClusters)
  b   = int(bSize)
  t   = int(iters)
  knn = int(kNN)
  tab = Reader( trainSet ).table()
  trn = tab.sample(10000)
  tst = tab.sample(10000)

  out( "Training : \n" ) 
  out( "  Clusters : " + cstr( k, "b" ) + "\n")
  out( "  Batch Sz : " + cstr( b, "b" ) + "\n")
  out( "  Iter Cnt : " + cstr( t, "b" ) + "\n")
  out( "  K Nghbrs : " + cstr( knn, "b" ) + "\n")
  out( "  trainSet : " + cstr( trainSet, "b" ) + "\n")
  out( "  testSet  : " + cstr( testSet, "b" ) + "\n") 
        
  t0 = clock() #python on windows needs to use clock, 
               #since the system clock is different. 
               #clock on *nix seems to work fine, so clock seems to be
               # more portable in general. 

  C = trn.sample( k, shallowCopy=False )   # 0. initial random centers
  V = [0] * len(C)                         # 1. size of the current cluster
  for i in xrange( t ) :                   # 2. for all iters
    p = int(i/t * 50) + 1                  # _. show the percent complete. 
    out("\r  [" + ( "#" * p ) + ("-" * (50-p)) + "]", color="b" )
    M = trn.sample( b )                    # 3. random samples from data set  
    D = [ C.closesti( k ) for k in M ]    # 4. closest center of each sample
    
    for x,c in zip(M,D) :                  # 5,6. for each sample and closest center
      if isinstance( c, list) : c = c[0]   # if I got more than one center
      c=c[0]
      V[c] += 1                            # 7. grow the center
      C.blendRow(c, x, 1/V[c] )            # 8,9. blend the center

  t1 = clock()
  out( "\n  Done!\n" ) 
  out( "\n  Time elpased : " + cstr( t1 - t0 , "b" ) + "\n\n" ) 
  out( "\nTesting : " )

  out("=== Predictions on test data ===\n\n")
  out(" inst#     actual  predicted error prediction\n")

  value_count = 1
  line_number = 1
  value_map   = {}

  t0 = clock()
  for row in tst : 
    closest = C.closest( row )[0]
    pred = tuple(C.getDependentValues( closest ))
    expt = tuple(C.getDependentValues( row     ))

    if pred not in value_map :
      value_map[ pred ] = value_count
      value_count += 1

    if expt not in value_map : 
      value_map[expt] = value_count
      value_count +=1

    preds = str( value_map[ pred ] )
    expts = str( value_map[ expt ] ) 
    reslt = "1" if pred == expt else "0"

    out.write( "%5s %5s %5s %1s\n" % ( line_number, expts, preds, reslt ) )
  t1 = clock() 
 
  out( "  Time elapsed : " + cstr( t1 - t0, "b" ) + "\n" )
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

  MiniBatchKNN( k, b, t, knn, trn, tst ) 

      
  
  
  
