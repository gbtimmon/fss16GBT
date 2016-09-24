from __future__ import print_function
import Table
import sys

tab = Table.CSVReader( sys.argv[1] ).table()
f1 = tab.furthest(0)
c1 = tab.closest(0)
f2 = tab.furthest(1)
c2 = tab.closest(1)

print( tab ) 
print( tab.dataStr() )

print( "\nROW 0 :",  tab[0])
print( "\nFurthest : \n", tab.furthest(0).dataStr() )
print( "\nClosest : \n", tab.closest(0).dataStr() )
print()
print( "\nROW 1 :",  tab[1])
print( "\nFurthest : \n", tab.furthest(1).dataStr() )
print( "\nClosest : \n", tab.closest(1).dataStr() )


print( "\nROW 0 :",  tab[0])
print( "\nFurthest : \n", tab.furthest(tab[0]).dataStr() )
print( "\nClosest : \n", tab.closest(tab[0]).dataStr() )
print()
print( "\nROW 1 :",  tab[1])
print( "\nFurthest : \n", tab.furthest(tab[1]).dataStr() )
print( "\nClosest : \n", tab.closest(tab[1]).dataStr() )
