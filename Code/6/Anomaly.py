from __future__ import print_function, division
from Table import Reader, Table
from IncrementalNB import IncrementalNB
from O import o

import sys

class NBAnomalyDetector(o): 

  def __init__( self, firstEra, secondEra ) : 
    super(o, self).__init__()
    self.NB  = IncrementalNB( firstEra.header, initialSet=firstEra )
    self.era = [[self.NB.predict(x)[1] for x in secondEra]]
    self.NB.train(secondEra)
    

  def detect( self, era ) : 
    pred = [ self.NB.predict(x)[1] for x in era ]
    self.era.append( pred ) 
    self.NB.train( era ) 
    return  a12( self.era[-2], self.era[-1] )
    
    
The=o(cohen=0.3, small=3, epsilon=0.01,
      width=50,lo=0,hi=100,conf=0.01,b=1000,a12=0.56)
    

 
  
# Stolen from the stats.py
# script in .ninja. 

def a12(lst1,lst2):
  "how often is x in lst1 more than y in lst2?"
  def loop(t,t1,t2): 
    while t1.j < t1.n and t2.j < t2.n:
      h1 = t1.l[t1.j]
      h2 = t2.l[t2.j]
      h3 = t2.l[t2.j+1] if t2.j+1 < t2.n else None 
      if h1>  h2:
        t1.j  += 1; t1.gt += t2.n - t2.j
      elif h1 == h2:
        if h3 and h1 > h3 :
            t1.gt += t2.n - t2.j  - 1
        t1.j  += 1; t1.eq += 1; t2.eq += 1
      else:
        t2,t1  = t1,t2
    return t.gt*1.0, t.eq*1.0
  #--------------------------
  lst1 = sorted(lst1, reverse=True)
  lst2 = sorted(lst2, reverse=True)
  n1   = len(lst1)
  n2   = len(lst2)
  t1   = o(l=lst1,j=0,eq=0,gt=0,n=n1)
  t2   = o(l=lst2,j=0,eq=0,gt=0,n=n2)
  gt,eq= loop(t1, t1, t2)
  return gt/(n1*n2) + eq/2/(n1*n2)  >= The.a12

if __name__ == '__main__' : 
  NBAnomalyDetector( sys.argv[1], eraSize=100)
