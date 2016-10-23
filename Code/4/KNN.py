from __future__   import division, print_function
from Table        import Table, Reader
from XStream      import XStream, cstr
from math         import floor
from time         import clock
from PrintResults import print_results
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

def KNN( k, trainSet, testSet, log=sys.stdout ) :

  #Cusomize the output streams
  out = XStream( sys.stdout, auto_flush=True, color="w" )
  err = XStream( sys.stderr, auto_flush=True, color="r" )
  
  k   = int(k)
  tab = Reader( trainSet ).table()
  trn = tab.sample(100)
  tst = tab.sample(100)

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

  t0 = clock()
  rslt = [ ( x, trn.closest(x, n=k)) for x in tst ]
  t1 = clock()
  out( "  Time elapsed : " + cstr( t1 - t0, "b" ) + "\n" )

  print_results( trn, rslt, stream=out )

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

      
  
  
  
