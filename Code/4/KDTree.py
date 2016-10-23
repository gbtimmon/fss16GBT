from __future__ import print_function
from Table import Table, Reader
from O import o 
from time import clock
from ResultSet import ResultSet
import collections 
__DOC__=(
"""
   KDTree

   @1    training inputs
   @2    testing inputs
"""
)

class Node () : 
  def __init__(i): 
    i.row, i.index, i.left, i.right = None, None, None, None

class KDTree(o) : 

  def __init__( i, table, shallowCopy=False ) : 

    super( KDTree, i).__init__()

    i.algorithm = "KDTree" 
    if not isinstance( table, Table) :
       table = Reader( table ).table()

    i.set  = table.copy() if shallowCopy else table.deepcopy()
    i.size = len( i.set )

    cols    = [ x for x in i.set.header if not x.isDep() ]
    cur_col = -1 

    i._tree = Node() 

    t0 = clock()
    worklist = [ (i._tree, table)  ]
    new_worklist = []

    while worklist :
      cur_col = (cur_col + 1 ) % len( cols)
      var = cols[cur_col]

      for t in worklist : 
        t[1].sort( key= lambda	r: r[var.pos] )
        median_idx = len(t[1]) // 2 
        left_table = t[1][:median_idx]
        rght_table = t[1][median_idx+1:]
        
        t[0].row   = t[1][median_idx]
        t[0].index = cur_col
        
        if( len(left_table) > 0 ) :
          t[0].left = Node()
          new_worklist.append( (t[0].left, left_table) )

        if( len(rght_table) > 0 ) :
          t[0].right = Node()
          new_worklist.append( (t[0].right, rght_table) )

      worklist = new_worklist
      new_worklist = []
    
    t1 = clock()
    i.time = t1 - t0
        
  def nn( i, dest ) : 
    best_row  = None
    best_dist = float('inf')
    
    worklist = [i._tree]
    while worklist :
      node = worklist.pop()
      dist = i.set.dist( dest, node.row )
      if( dist < best_dist ) :
        best_row = node.row
        best_dist = dist

      diff = dest[node.index] - node.row[node.index]
      close, away = (node.left, node.right) if diff <= 0 else (node.right, node.left)

      if close :
        worklist.append( close )
      if away and (diff**2 < best_dist ) :
        worklist.append( away  ) 
  
    return best_row, best_dist

  def test( i, test ) :
    if not isinstance( test, Table ) : 
      test = Reader( table ).table()

    t0 = clock()
    rslt = [( x, i.nn( x )[0]) for x in test ]
    t1 = clock()

    testObj = o()
    testObj.set = test
    testObj.size = len(test)
    testObj.time = t1 - t0 

    return ResultSet( i, testObj, rslt )
    
if __name__ == '__main__' : 
  import sys 

  if( len(sys.argv) < 3 ) :   
    print( __DOC__ )
    exit(1)   
  train = sys.argv[1]
  test  = sys.argv[2]
  
  tab = Reader(train).table().sample(100)
  test = Reader( test ).table().sample(100)

  t = KDTree( tab )
  r = t.test( test )

  print( r ) 
  print( r.info() )
