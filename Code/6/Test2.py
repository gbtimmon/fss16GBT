from __future__ import print_function, division 
from Table import Table, Reader
from Generator import Generator
from Anomaly import NBAnomalyDetector
from IncrementalNB import IncrementalNB
import sys

def median(lst):
    quotient, remainder = divmod(len(lst), 2)
    if remainder:
        return sorted(lst)[quotient]
    return sum(sorted(lst)[quotient - 1:quotient + 1]) / 2

tab = Reader( sys.argv[1] ).table()
gen = Generator( tab ) 
gen.setProb( (50,50) )

era = [(50,50,0)]*10 + [(10,30,60)]*10

inb = IncrementalNB( tab.header, initialSet=gen.getTable(100) )


idx = 1
for e in era : 
  gen.setProb(e)
  dat = gen.getTable(100) 
  rs = inb.test( dat ) 

  recall = [] 

  for k,v in rs.values.iteritems() : 
    bot = 0
    top = 0
    for r in rs.result : 
      if( r.expected == k and r.predicted == k ) : top+=1
      if( r.expected == k ) : bot+=1
    recall.append(top/bot)
  print("Era %2d : Recall = %3.2f, Probability = ( %2d, %2d, %2d )"%(idx, sum(recall)/len(recall),e[0],e[1],e[2]))

  from collections import defaultdict
  mp = defaultdict(list)
  for d in dat : 
    ret = inb.predict( d )
    mp[ret[0][0]].append( ret[1] )

  for k,v in mp.iteritems() : 
    print("    %10s median log-likelihood is %3.2f"%(k,median(v)))

  
  idx+=1
  inb.train( dat ) 
  


"""
ana = NBAnomalyDetector( gen.getTable( 100 ), gen.getTable(100) )
for e in eras :
   gen.setProb( e )  
   
   print( "Era ("+ str(e) + "):" + str(ana.detect( gen.getTable( 100 ) ) ) )
"""
    
