from __future__ import print_function, division
from Table      import Table, Reader 
from O          import o

import sys 
import random

class Generator(o) : 

  def __init__( self, table ) : 

    super(o,self).__init__()

    if not isinstance( table, Table ) : 
      table = Reader( table ).table()

    self.table = table
    self.subtable = []

    dv = [ x for x in table.header if x.isDep() ] 
 
    if( len(dv) > 1 ) : 
       raise NotImplemented( "MultiObjective not implemented" ) 

    dv = dv[0]
    
    #Split the tables by class var 
    temptable = table 
    for k in dv.stat.counts.keys() :
       yes, temptable = temptable.filter( lambda idx, row : row[dv.pos] == k )
       yes.shuffle() 
       self.subtable.append( yes ) 

    self.index = [0] * len(self.subtable)
    self.setProb( [1] * len(self.subtable) ) 

    for x in self.subtable : print( repr(x) ) 
    print( self.index )
    print( self.prob ) 
    
  def setProb( self, prob ) : 

    if ( len( prob ) > len( self.subtable ) ) : 
      raise ValueError("More probabilities than classes. \nThis dataset has %d classes"%(len(self.subtable)))

    sm = sum( prob )
    self.prob = tuple([ x / sm for x in prob ])

  def __iter__(self) :
    while True:
      yield self.getOneRow()

  def getTable( self, k ) : 
    return Table( self.getRows(k), header=self.table.header, shallowCopy=True )

  def getRows(self, k ):
    for _ in xrange(k) :
      yield self.getOneRow()

  def getOneRow(self ) : 
    r = random.random()
    i = 0 

    
    for x in self.prob : 
      if( r < x ) : 
        break
      else :
        r -= x
        i += 1

    idx = self.index[i]
    tab = self.subtable[i]

    if( idx == len( tab ) ) :
      tab.shuffle()
      idx = 0
      self.index[i] = 0

    self.index[i] += 1
    return tab[idx]
 
if __name__ == '__main__' : 
   g = Generator( sys.argv[1] ) 

   for t in [(0,0,25,75),(50,50),(25,25,25,25),(0,100,0,0,0,100)] :
     print()
     print("SET PROB : " + str(t) )
     print()
     g.setProb( t ) 
     for x in g.getRows(50) : 
       print(x)


