from Table import CSVReader 
import sys

tab = CSVReader( sys.argv[1] ).table()
print( tab ) 

tab2 = tab.copy()
print ( tab2 )

tab3 = tab.deepcopy()
print( tab3 )

tab[1][2] = "CHANGE ONE"
tab3[5][3] = "CHANGE TWO"

print( tab ) 
print( tab2 )
print( tab3 )
