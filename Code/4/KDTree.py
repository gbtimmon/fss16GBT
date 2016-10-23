from __future__ import print_function
from Table import Table, Reader
from time import clock
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

class KDTree( ) : 

  def __init__( i, table, shallowCopy=False ) : 

    i.table = table.copy() if shallowCopy else table.deepcopy()
    i.header = i.table.header
      
    i.iv    = [ x for x in i.header if not x.isDep() ]
    i.c_iv  = -1 

    def next_var( ) : 
      i.c_iv = (i.c_iv + 1) % len(i.iv)
      return i.iv[i.c_iv]

    i.tree = Node() 
    worklist = [ (i.tree, table)  ]
    new_worklist = []

    while worklist :
      var = next_var()
      for t in worklist : 
        t[1].sort( key= lambda	r: r[var.pos] )
        median_idx = len(t[1]) // 2 
        left_table = t[1][:median_idx]
        rght_table = t[1][median_idx+1:]
        
        t[0].row   = t[1][median_idx]
        t[0].index = i.c_iv
        
        if( len(left_table) > 0 ) :
          t[0].left = Node()
          new_worklist.append( (t[0].left, left_table) )

        if( len(rght_table) > 0 ) :
          t[0].right = Node()
          new_worklist.append( (t[0].right, rght_table) )

      worklist = new_worklist
      new_worklist = []
    
        
  def nn( i, dest ) : 
    best_row  = None
    best_dist = float('inf')
    
    worklist = [i.tree]
    while worklist :
      node = worklist.pop()
      dist = i.table.dist( dest, node.row )
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
    
if __name__ == '__main__' : 
  import sys 

  if( len(sys.argv) < 3 ) :   
    print( __DOC__ )
    exit(1)   
  train = sys.argv[1]
  test  = sys.argv[2]
  
  tab = Reader(train).table().sample(1000)
  t0 = clock()
  tre = KDTree( tab )
  t1 = clock()
  print("Training Time : ", str( t1 - t0 ) )
 
  test = Reader( test ).table().sample(1000)

  results = []
  t0 = clock()
  for i in test : 
    nn =  tre.nn(i) 
  t1 = clock()
  print("Testing Time : ", str( t1 - t0 ) )
