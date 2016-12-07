from __future__ import print_function, division
import sys
from Table      import Table, Reader
from math       import floor
import numpy    as np

def crossval( tab, num_of_crosses ) : 
  increment      = int( len(tab) / num_of_crosses ) 
  for i in range( num_of_crosses ) :
    table_range = lambda k,_ : k >= (increment*i) and k < ( increment*(i+1) )
    test,train = tab.filter( table_range, shallowCopy=True )
    yield train

