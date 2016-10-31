from __future__ import print_function, division 
from Table import Table, Reader
from Generator import Generator
from Anomaly import NBAnomalyDetector
from IncrementalNB import IncrementalNB
import sys

tab = Reader( sys.argv[1] ).table()
gen = Generator( tab ) 
gen.setProb( (50,50) )

era = [(50,50,0)]*10 + [(10,30,60)]*10


idx = 1
gen.setProb((50,50,0))
ana = NBAnomalyDetector( gen.getTable( 100 ), gen.getTable(100) )
for e in era :
   gen.setProb( e )  
   dat = gen.getTable(100)
   ret = ana.detect( dat ) 
   print( "Era %d : anomaly detected %s"%(idx, str(ret)))
   idx +=1

   
    
