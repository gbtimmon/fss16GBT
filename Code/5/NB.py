from __future__ import division, print_function
from O import o
import inspect
from collections import defaultdict
from Table import Table, Reader, Num, Sym
from time import clock
from math import log, sqrt, pi, exp
from ResultSet import ResultSet

def gauss(x, mu, sigma):
    u = (x-mu)/abs(sigma + 10e-50) 
    y = (1/( (sqrt(2*pi)*abs(sigma)) + 10e-50))*exp(-u*u/2)
    return y

class NB(o) : 
  def __init__( self, train, target=None, pdf="gauss" ) : 

    super(NB, self).__init__()
    self.set       = train if isinstance( train, Table ) else Reader( train ).table()
    self.size      = len(train)
    self.pdf       = pdf 
    self._pdf      = gauss if pdf == "gauss" else None
    self.algorithm = "Niave Bayes"

    t0 = clock()

    deps = [ x for x in self.set.header if x .isDep() ]

    if( len(deps) > 1 ) : 
      sys.stderr.write("Multiobjective not implemented!")
      exit(1)
    
    self._subtable = []

    pos = deps[0].pos
    d   = deps[0].stat.counts

    for k in d.keys() :
      new_tab,_ = self.set.filter( lambda idx, row : row[pos] == k )
      self._subtable.append( new_tab ) 
   
    self.time = clock() - t0
 
  def predict(self,  row ) : 
    best   = -1000000000000000
    bestdv = None
   
    for table in self._subtable : 
      prob = 0 
      p = len(table) / len(self.set) # P( target )
      prob += 0 if p == 0 else log(p)

      for r,h in zip( row, table.header ) :
        if h.isDep() : 
          continue
   
        if isinstance( h.stat, Num ) :
          p = self._pdf( r, h.stat.mu, h.stat.sd() )
          prob += 0 if p == 0 else log(p)
        else :
          symbol_count  = 0 if r not in h.stat.counts else h.stat.counts[r] 
          p = symbol_count / len( table ) 
          prob += 0 if p == 0 else log(p)

      if prob > best : 
        best   = prob 
        bestdv = table.getDependentValues( table[0] )
   
    return bestdv 

  def test(self, test ) : 

    testObj = o()
    if not isinstance( test, Table ):
      test = Reader( test ).table()

    t0 = clock()
    rslt = [ (row, self.predict(row) ) for row in test ]
    testObj.time = clock() - t0
    testObj.set  = test
    testObj.size = len( test ) 
    
    return ResultSet( self, testObj, rslt )


if __name__ == '__main__' :
  import sys

  tab = Reader( sys.argv[1] ).table()
  nb = NB( tab ) 
 
  tab = Reader( sys.argv[2] ) .table()
  rs = nb.test( tab )
  print( rs.info() )
 
      
      

    

    
