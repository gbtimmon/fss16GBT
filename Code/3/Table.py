import FileReader
import math

class Table:
  def __init__( self, fileName ) : 
    self.filename = fileName
    self.rowCount = 0

    reader = FileReader.factory( fileName )

    self.header = Header(reader.next())
    self.data   = []
    for x in reader :
      self.rowCount += 1
      self.header.update(x)
      self.data.append(x)
      
  def __str__(self) :
     return "\n     File Name :" + str(self.filename) + "\n     Row Count : " + str(self.rowCount) + "\n\n" + str(self.header)

     
class Header:

  def __str__(self) :
    
    return (
      ("%20s | %-5s  %-5s  %-20s  %-10s  %-10s  %-10s  %-10s  %-10s\n" % ( "NAME", "ETRPY", "M-CNT", "MODE", "MU", "M2", "SD", "MIN", "MAX"))
      + (" "*5 +"-" * 16 + "+" + ("-"*75) + "\n")
      + "".join( [ str(x) for x in self.obj ])
    )
    
  def __init__( self, cols ) : 
    self.rowCount = 0
    self.obj = [ _Header(x) for x in cols ]

  def names ( self ) :
    return [ x.name for x in self.obj ] 

  def syms ( self ) : 
    return [ x.symbol for x in self.obj ]

  def update( self, row ) :
    self.rowCount += 1
    map( lambda a, b: a.symbol.add(b), self.obj, row )
    map( lambda a, b: a.number.add(b), self.obj, row )
    
    
class _Header:
  def __init__( self, name) : 

    self.number = Num()
    self.symbol = Sym()
    self.name   = name

  def __str__(self) :
    return ( 
           ( "%20s | %s %s\n" % ( str(self.name), self.symbol.rowStr(), self.number.rowStr() ))
    )

     
class Num:

  def rowStr( self ) :
    if( self.invalid ) :
      return (("%10s  %10s  %10s  %10s  %10s") % ( "-", "-","-","-","-" ))
    else :
      return (("%10.4f  %10.4f  %10.4f  %10.4f  %10.4f") % ( self.mu,  self.m2, self.sd(), self.min, self.max))

  def __init__( self ) :
    self.mu      = 0
    self.n       = 0
    self.m2      = 0
    self.max     = -sys.maxint - 1
    self.min     = sys.maxint
    self.invalid = False

  def add( self, x):
    if( self.invalid ) :
      return 

    try :
      x = float(x)
    except Exception:
      self.invalid = True
      return

    self.n += 1
    self.max = max( self.max, x )
    self.min = min( self.min, x )

    delta    = x - self.mu
    self.mu  += delta/self.n
    self.m2  += delta*(x - self.mu)
    return x 

  def sub(i,x): 

    "No check for item existence here might be a problem"
    "add(7) add(7) add(7) sub(4) -- what would my data even mean??"

    self.n   = max(0, self.n - 1)
    delta = x - self.mu
    self.mu  = max(0,self.mu - delta/self.n)
    self.m2  = max(0,self.m2 - delta*(x - self.mu))

  def sd( self ):
    return 0 if self.n <= 2 else (self.m2/(self.n - 1))**0.5

from collections import defaultdict
from collections import OrderedDict

class Sym():

  def rowStr( self ) :
    return (("%5.4f  %5s  %-20s") % ( self.ent(), str(self.most),  str(self.mode)))

  def __init__( self ):
     self.counts, self.most, self.mode, self.n = {},0,None,0

  def add(i,x):
    i.n += 1
    new = i.counts[x] = i.counts.get(x,0) + 1
    if new > i.most:
      i.most, i.mode = new,x
    return x

  def ent(self):
    tmp = 0
    for val in self.counts.values():
      p = float(val)/float(self.n)
      if p:
        tmp -= p*math.log(p,2)
    return tmp  

if __name__ == '__main__' : 
  import sys
  print Table(sys.argv[1] )
