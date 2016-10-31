from __future__ import division, print_function
from O import o
import inspect
from collections import defaultdict
from Table import Table, Reader, Num, Sym, Row
from time import clock
from math import log, sqrt, pi, exp
from ResultSet import ResultSet

def gauss(x, mu, sigma):
    u = (x-mu)/abs(sigma + 10e-50) 
    y = (1/( (sqrt(2*pi)*abs(sigma)) + 10e-50))*exp(-u*u/2)
    return y

class IncrementalNB(o) : 
  def __init__( self, header, initialSet=None, pdf="gauss" ) : 

    super(IncrementalNB, self).__init__()

    self.set       = Table( [], header=header, shallowCopy=True )
    self.pdf       = pdf 
    self._pdf      = gauss if pdf == "gauss" else None
    self.algorithm = "Niave Bayes"
    self._subtable = {}

    t0 = clock()

    if initialSet is not None : 
      if not isinstance( initialSet, Table ) :
        initialSet = Reader( initialSet ).table()
      self.train( initialSet )

    self.time = clock() - t0

  def train( self, ele ) : 
    """
    Public Wrapper function for _train to handle polymorphic input (Table or Row or [] )
    """
    if isinstance( ele, Table ) :
      for x in ele : self._train( x )     
    else : 
      self._train( ele ) 

  def _train( self, row ) : 
    """
    _train add a row to the knowledge base of the NB
    """
    dv   = self.set.getDependentValues( row )
    nrow = Row( row )  
    if len(dv) > 1 :
      raise NotImplemented("Multi Objective Niave Bayes was not implemented")

    dv = dv[0]

    if dv not in self._subtable:
      self._subtable[dv] = Table([], header=self.set.header, shallowCopy=True)
   
    self._subtable[dv]( nrow )
    self.set( nrow ) 
 
  def predict(self,  row, train=False ) : 
    best   = -1000000000000000
    bestdv = None
   
    for table in self._subtable.values() : 
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

    if train :
      self.train( row )
   
    return ( bestdv, best ) 

if __name__ == '__main__' :
  import sys

  tab = Reader( sys.argv[1] ).table().sample(1000)
  nb = NB( tab ) 
 
  tab = Reader( sys.argv[2] ) .table().sample(100)
  rs = nb.test( tab )
  print( rs.info() )
 
      
      

    

    
