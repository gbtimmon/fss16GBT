#!python
import sys
import numpy as np

from IntrinsicDim import * 
from inDim        import * 
from collections  import defaultdict
from scipy.io     import arff
from Table        import Table, Reader 
from Crossval     import crossval

table="../data/coc81.arff"

k = int(sys.argv[1])

t = Reader( table, ignoreCols=(0,23,24,25,26), sep=" " ).table()

for r, row in enumerate( t.data ) : 
  for c, col in enumerate( row ) : 
    if( col == 'vl' ) : t.data[r][c] = 0
    if( col == 'l' ) : t.data[r][c] = 1
    if( col == 'n' ) : t.data[r][c] = 2
    if( col == 'h' ) : t.data[r][c] = 3
    if( col == 'vh' ) : t.data[r][c] = 4
    if( col == 'xh' ) : t.data[r][c] = 5


med_id( t, k, 2*k ) 

t2 = Reader( table, ignoreCols=(0,23,25,26), sep=" " ).table()

for r, row in enumerate( t2.data ) : 
  for c, col in enumerate( row ) : 
    if( col == 'vl' ) : t2.data[r][c] = 0
    if( col == 'l' ) : t2.data[r][c] = 1
    if( col == 'n' ) : t2.data[r][c] = 2
    if( col == 'h' ) : t2.data[r][c] = 3
    if( col == 'vh' ) : t2.data[r][c] = 4
    if( col == 'xh' ) : t2.data[r][c] = 5

a = med_id( t, k, 2*k )
b = med_id( t2, k, 2*k ) 

print( a , b ) 

