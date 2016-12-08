#!python
import sys
import numpy as np

from pca          import *
from collections  import defaultdict
from scipy.io     import arff
from Table        import Table, Reader 
from Crossval     import crossval

table="../data/coc81.arff"

t = Reader( table, ignoreCols=(0,23,24,25,26), sep=" " ).table()

for r, row in enumerate( t.data ) : 
  for c, col in enumerate( row ) : 
    if( col == 'vl' ) : t.data[r][c] = 0
    if( col == 'l' ) : t.data[r][c] = 1
    if( col == 'n' ) : t.data[r][c] = 2
    if( col == 'h' ) : t.data[r][c] = 3
    if( col == 'vh' ) : t.data[r][c] = 4
    if( col == 'xh' ) : t.data[r][c] = 5

pca( t, 0.025 ) 
pca( t, 0.015 ) 
a = pca( t, 0.005, plot=True ) 


t = Reader( table, ignoreCols=(0,23,25,26), sep=" " ).table()

for r, row in enumerate( t.data ) : 
  for c, col in enumerate( row ) : 
    if( col == 'vl' ) : t.data[r][c] = 0
    if( col == 'l' ) : t.data[r][c] = 1
    if( col == 'n' ) : t.data[r][c] = 2
    if( col == 'h' ) : t.data[r][c] = 3
    if( col == 'vh' ) : t.data[r][c] = 4
    if( col == 'xh' ) : t.data[r][c] = 5

pca( t, 0.025  ) 
pca( t, 0.015  ) 
b = pca( t, 0.005, plot=True  ) 

print ( a ) 
print ( b ) 

print( [ x - y for x,y in zip( a, b ) ] ) 
print( sum([ x - y for x,y in zip( a, b ) ] ) )
