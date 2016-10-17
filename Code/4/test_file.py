from __future__ import print_function
from Table import Table, Reader

tab = Reader( "../../../ninja/data/weather.csv" ).table()

print( *tab.knn(3,n=4), sep="\n" )
