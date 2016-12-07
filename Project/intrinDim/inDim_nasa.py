#!python
import sys
import hub_toolbox
import numpy as np

from IntrinsicDim import * 
from inDim        import * 
from collections  import defaultdict
from scipy.io     import arff
from Table        import Table, Reader 

table="../data/nasa93.arff"

k = int( sys.argv[1] ) 
t = Reader( table, ignoreCols=(0,23,24,25,26), sep="," ).table()

for r, row in enumerate( t.data ) : 
  for c, col in enumerate( row ) : 
    if( col == 'vl' ) : t.data[r][c] = 0
    if( col == 'l' ) : t.data[r][c] = 1
    if( col == 'n' ) : t.data[r][c] = 2
    if( col == 'h' ) : t.data[r][c] = 3
    if( col == 'vh' ) : t.data[r][c] = 4
    if( col == 'xh' ) : t.data[r][c] = 5

a = med_id( t, k, k*2 ) 

t = Reader( table, ignoreCols=(0,23,25,26), sep="," ).table()

for r, row in enumerate( t.data ) : 
  for c, col in enumerate( row ) : 
    if( col == 'vl' ) : t.data[r][c] = 0
    if( col == 'l' ) : t.data[r][c] = 1
    if( col == 'n' ) : t.data[r][c] = 2
    if( col == 'h' ) : t.data[r][c] = 3
    if( col == 'vh' ) : t.data[r][c] = 4
    if( col == 'xh' ) : t.data[r][c] = 5


b = med_id( t, k, k*2 ) 

print( list( zip( a, b ) ) ) 


