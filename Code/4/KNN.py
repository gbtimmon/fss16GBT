from __future__  import division, print_function
from Table       import Table, Reader
from XStream     import XStream, cstr
from math        import floor
from time        import clock
import sys

__DOC__=(
"""
KNN
  Author : Greg Timmons
  Date   : Fall 2016

  Input :
    @1     nCLusters : number of clusters
    @2     trainSet  : training set
    @3     testSet   : testing set

"""
)

def KNN( nClusters, trainSet, testSet, log=sys.stdout ) :

  #Cusomize the output streams
  out = XStream( sys.stdout, auto_flush=True, color="w" )
  err = XStream( sys.stderr, auto_flush=True, color="r" )
  
  k   = int(nClusters)
  tab = Reader( trainSet ).table()
  trn = tab.sample(10000)
  tst = tab.sample(10000)

  out( "Training : \n" ) 
  out( "  K Nghbrs : " + cstr( k, "b" ) + "\n")
  out( "  trainSet : " + cstr( trainSet, "b" ) + "\n")
  out( "  testSet  : " + cstr( testSet, "b" ) + "\n") 
        
  t0 = clock() #python on windows needs to use clock, 
               #since the system clock is different. 
               #clock on *nix seems to work fine, so clock seems to be
               # more portable in general. 
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
    closest = trn.closest( row, n=1 )[0]
    pred = tuple(trn.getDependentValues( closest ))
    expt = tuple(trn.getDependentValues( row     ))

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
    trn = sys.argv[2]       
    tst = sys.argv[3] 
  except : 
    sys.stderr.write( cstr(" Illegal Arguments\n greater than", "r") )
    sys.stderr.write( __DOC__ )
    exit(1)

  KNN( k, trn, tst ) 

      
  
  
  
