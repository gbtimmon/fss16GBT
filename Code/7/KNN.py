from __future__ import division, print_function
from Table      import Table, Reader
from O          import o
from math       import floor
from time       import clock
from ResultSet  import ResultSet
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

class KNN(o) :
  def __init__( i, trainSet ) : 
    super( KNN, i).__init__()

    i.algorithm    = "KNN"
    i.set     = trainSet if isinstance( trainSet, Table ) else Reader( trainSet ).table()
    i.size    = len( i.set )
    i.time = 0

  def test(i, k, testSet ) :

    testObj   = o()
    testObj.k = k

    if not isinstance( testSet, Table ):
      testObj.set = Reader(testSet).table()
    else : 
      testObj.set = testSet

    testObj.size = len( testObj.set )

    t0 = clock()
    rslt = [ ( x, i.set.closest(x, n=testObj.k)) for x in testObj.set ]
    t1 = clock()

    testObj.time = t1 - t0

    return ResultSet( i, testObj, rslt )
   

if __name__ == '__main__' : 
  try : 
    k   = int( sys.argv[1] )       
    trn = Reader(sys.argv[2]).table().sample(100)
    tst = Reader(sys.argv[3]).table().sample(100)
  except : 
    sys.stderr.write( cstr(" Illegal Arguments\n greater than", "r") )
    sys.stderr.write( __DOC__ )
    exit(1)

  test = KNN( trn )
  resl = test.test( k, tst )
  print( resl.info() ) 

      
  
  
  
