from __future__ import print_function
from Table import Table, Reader

tab = Reader( "../../../ninja/data/weather.csv" ).table()
 
print( *tab, sep="\n" ) 

tab.sort( key=lambda x : x[4])

print( *tab, sep="\n" ) 
