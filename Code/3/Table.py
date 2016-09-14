import FileReader
import math
import sys
import re

sys.dont_write_bytecode = True

class Table:

  def __len__( self ) :
    return self.rowCount

  def __init__( self, **kwargs ) : 

    self.filename = kwargs["fileName"]
    self.rowCount = 0

    reader = FileReader.factory( kwargs )

    self.header = Header(reader.next())
    self.data   = []
    for x in reader :
      self.rowCount += 1
      self.header.update(x)
      self.data.append(x)

  def __getitem__( self, tup) :

    i,j = tup

    if( i == -1 ) : 
      if( j == None ) : return self.header
      return self.header[j]

    if( j == None ) : return self.data[i]
    return self.data[i][j]
  
  def dist( self, a, b, f=2 ) :
    d = 0
    n = len( self.header )
    s = 0

    if( n == 0 ) : return None

    for col in xrange(n):
       hd = self.header[ col ]
       v1 = self[ a, col ]
       v2 = self[ b, col ]
     
       if( v1 is None and v2 is None ): continue
       if( v1 is None ) : v1 = hd.furthest(v2)
       if( v2 is None ) : v2 = hd.furthest(v1)
       s += hd.dist( v1, v2) ** f

    return (( float(s) ** (1.0/float(f)))/(float(n)**(1.0/float(f))))

  def __str__(self) :
     return "\n     File Name :" + str(self.filename) + "\n     Row Count : " + str(self.rowCount) + "\n\n" + str(self.header)


"""
  Header class

  Stores a set of meta data for the table. 
  Each column is a _Header object
    each _header object contains a Sym and Num object to store requisite metadata. 
    If any non-num value is recieved then the Num object is deactivate since there is a non-num value

"""     
class Header:

  def __getitem__(self, i):
    return self.obj[i]

  def __len__(self) : 
    return len(self.obj)

  def __str__(self) :
    
    return (
      ("%20s | %-5s  %-5s  %-20s  %-10s  %-10s  %-10s  %-10s  %-10s\n" % ( "NAME", "ETRPY", "M-CNT", "MODE", "MU", "M2", "SD", "MIN", "MAX"))
      + (" "*5 +"-" * 16 + "+" + ("-"*75) + "\n")
      + "".join( [ str(x) for x in self.obj ])
    )
    
  def __init__( self, cols ) : 
    
    cols = map( lambda x: re.sub("[^a-zA-Z0-9_ ]","",x), cols )
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

  def norm( self, x ) :
    return self.symbol.norm(x) if ( self.number.invalid ) else self.number.norm(x) 

  def dist( self, x, y):
    return self.symbol.dist(x,y) if ( self.number.invalid ) else self.number.dist(x,y) 

  def furthest( self, x ) : 
    return self.symbol.furthest(x) if ( self.number.invalid ) else self.number.furthest(x) 

     
"""
   Num Class

   Stores the number metadata. 

"""
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

  def norm( self, x ) :
    denom = self.max - self.min
    if( denom == 0 ) : return 0

    norm = x - self.min / denom
    return max( min ( norm, 1), 0 )

    
  def dist( self, a, b ) : 
    return abs(self.norm(b) - self.norm(a))

  def furthest ( self, x ) :
    return self.max if x <(self.max-self.min)/2 else self.min

  def sd( self ):
    return 0 if self.n <= 2 else (self.m2/(self.n - 1))**0.5


"""
    Sym Class

    Stores the symbols metadata. 

"""
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

  def norm( self, x )     : return x
  def dist( self, x, y)   : return 0 if x == y else 1
  def furthest( self, x ) : return None

  def ent(self):
    tmp = 0
    for val in self.counts.values():
      p = float(val)/float(self.n)
      if p:
        tmp -= p*math.log(p,2)
    return tmp  

if __name__ == '__main__' : 
  import sys
  tab = Table(fileName=sys.argv[1], sep = ",", missing="?" )
  print tab[1,4]
  for x in xrange( len( tab ) ) : 
    for y in xrange( len( tab ) ) :
      print x, y, tab.dist(x,y)
