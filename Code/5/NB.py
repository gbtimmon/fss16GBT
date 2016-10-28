from __future__ import division
from O import o
from collections import defaultdict
from Table import Table, Reader 
from math import log
from ResultSet import ResultSet

class NB(o) : 
  def __init__( self, train ) : 
    super(NB, self).__init__()
    self.set       = train if isinstance( train, Table ) else Reader( train ).table()
    self.size      = len(train)
    self.algorithm = "Niave Bayes"
    self._chance   =  defaultdict(int)
    self._target   = {}
    self._eps      = 0.000000001

    for row in self.set : 
      dv = tuple(self.set.getDependentValues(row))

      if dv not in self._target : 
        self._target[dv] = 0 

      self._target[dv] += 1

      for col in self.set.header : 
        tup1 = ( col.name, row[col.pos], dv )
        tup2 = ( col.name, row[col.pos])

        if tup1 not in self._chance :
          self._chance[tup1] = 0

        if tup2 not in self._chance :
          self._chance[tup2] = 0

        self._chance[tup1] += 1
        self._chance[tup2] += 1
 
  def classify(self,  row ) : 
    best   = -1000000000000000
    bestdv = None
   
    for target, value in self._target.iteritems() :

      prob = log( (value +self._eps) / self.size )
      for column in self.set.header : 
        lkp = ( column.name, row[column.pos], target )
        top = self._chance[( column.name, row[column.pos], target)]
        prob += log( ( top + self._eps ) / value )

      if prob > best : 
        best = prob
        bestdv = target

    return bestdv

  def test(self, test ) : 

    
    if not isinstance( test, Table ):
      test = Reader( test ).table()

    rslt = [ (row, self.classify(row) ) for row in test ]

    testObj = o()
    testObj.set  = test
    testObj.size = len( test ) 
    
    return ResultSet( self, testObj, rslt )


if __name__ == '__main__' :
  import sys

  tab = Reader( sys.argv[1] ).table()
  nb = NB( tab.sample(10) ) 
 
  tab = Reader( sys.argv[2] ) .table()
  rs = nb.test( tab )
  print( rs.info() )
 
      
      

    

    
