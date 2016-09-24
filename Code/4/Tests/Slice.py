from Table import CSVReader 
import sys
sys.dont_write_bytecode = True


tab = CSVReader( sys.argv[1] ).table()
print( tab ) 

for i in range( len(tab ) ) :
   print( tab.sample(i) )
