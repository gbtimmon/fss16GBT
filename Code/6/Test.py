from __future__ import print_function, division 
from Table import Table, Reader
from Generator import Generator
from Anomaly import NBAnomalyDetector
import sys

tab = Reader( sys.argv[1] ).table()
gen = Generator( tab ) 
gen.setProb((50,50))
ana = NBAnomalyDetector( gen.getTable( 100 ), gen.getTable(100) )


eras =[(50,50,0)]*8 + [(10,30,60)]*10

for e in eras :
   gen.setProb( e )  
   print( "Era ("+ str(e) + "):" + str(ana.detect( gen.getTable( 100 ) ) ) )
    
