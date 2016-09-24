###
# Table v2.0
#
# This version of the code add a lot of features over our first version
# including shallow table copy, an improved table creation pattern and 
# inversion of the FileReader pattern so the FileReader will build the table
# rather then the table using the FileReader which seems to simplfy the code. 
#
###

from __future__ import print_function
import math
import sys
import re

sys.dont_write_bytecode = True

def cache( func ) : 
  """
  Some data from tables is only needed to be computed once. 
  if this is the cache (hey look I made a pun), then we will
  return a saved value. Right now only support no input functions
  but could be expanded to consider inputs. 
  """
  retVal = None
  def memory( ) :
     if retVal == None:
        retVal = func()
     return retVal
    
class Stream : 
   def next( i ) : return i.__iter__().next()

class Vector : 
   def __len__( i )           : return len( i.data ) 
   def __getitem__( i , x )   : return i.data[x]
   def __iter__( i )          : return i.data.__iter__()
   def __setitem__( i, x, y ) : i.data[x] = y
   def __str__( i )           : return i.data.__str__()
   def __repr__( i )          : return i.data.__repr__()

class CSVReader( Stream ) : 

  def __init__ ( i, filename, sep="," ) : 
    
    i.filename   = filename
    i.sep        = sep
    i.missing    = "?"
    i.curLine    = 0
    i.fileHandle = open( i.filename, "r" ) if( i.filename != None ) else sys.stdin
   
  def __iter__(i):
    for line in i.fileHandle :
      line = line.strip()
      if( len(line) == 0 ) : continue
      if( line[0] == "%")  : continue
      yield Row( map( i.wrangle, line.split( i.sep ) ) )

  def wrangle(i, inv ) :

    if( int == i.missing ) : return None

    try  : return int(inv)
    except Exception : pass
 
    try  : return float(inv)
    except Exception : pass

    inv = inv.strip()
    return str(inv)

  def table( i ) : 
    return Table( i )

class Row( Vector ):
  """
  Row Class to assist in shallow copy of tables if desired. 
  Control of Shallow copy can be control in the Row class.
  """
  idGen = 0 
  def __init__(i, data) : 
     i.data = data
     i.id   = Row.idGen = Row.idGen + 1
     

class Table(Vector):
  
  idGen = 0

  def __init__( i, stream, shallowCopy=True ) : 
    i.rowCount = 0 
    i.id       = Table.idGen = Table.idGen + 1 
    i.header   = Header( stream.next() )
    i.data     = []

    for x in stream : 
      i.rowCount += 1
      i.header.add(x)
      i.data.append(x)

  def furthest( i, x ) : 
    arr = i.dist(x)
    return [ i for i,j in enumerate(arr) if j == max(arr) ] 

  def closest( i, x ) : 
    arr = i.dist(x)
    arr_min = min( [ k for k in arr if k > 0 ] )
    return [ j for j,k in enumerate(arr) if k == arr_min ]

  def dist( i, a, b=None, f=2 ) :

    def _dist( i, a, b, f=f ) :
      """ Helper Function
      This is an iimplementation of AHAs algorithm.
      """

      d = 0
      n = len( i.header )
      s = 0

      if( n == 0 ) : return None

      for col in xrange(n):
         hd = i.header[ col ]
         if( hd.isDep() ) : continue

         v1 = i[ a ][ col ]
         v2 = i[ b ][ col ]

         if( v1 is None and v2 is None ): continue
         if( v1 is None ) : v1 = hd.furthest(v2)
         if( v2 is None ) : v2 = hd.furthest(v1)
         s += hd.dist( v1, v2) ** f

      return (( float(s) ** (1.0/float(f)))/(float(n)**(1.0/float(f))))
    "END HELPER FUNCTION"

    if b is not None :
      return _dist(i, a, b=b)

    return [ _dist(i, a, x) for x in range(len(i))]

class Header(Vector) : 
  def __init__( i, col ) : 
    i.data = [ _Header(col[x], x) for x in xrange(len(col)) ]

  @cache
  def names( i ) :
    return [x.name for x in i.cols ]

  def add( i, row ) :
    for a,b in zip( i, row ) : a.add(b)   

  def __str__( i ) : 
    return str([str(x) for x in i.data ])
 

class _Header:

  def isDep( i )      : return i.dep
  def norm( i, x )    : return i.stat.norm( x )
  def dist( i, x, y ) : return i.stat.dist( x, y)
  def furthest( i, x ): return i.stat.furthest( x ) 

  def __init__ ( i, name, pos) : 
    i.pos  = pos
    i.dep  = False
    i.stat = None
    i.name = name
    i.stat = None

  def add( i, x ) : 
    if i.stat == None :
      try : 
        x = float( x ) 
        i.stat = Num()
      except : 
        x = str( x )
        i.stat = Sym()
      i.stat.add( x ) 

  def __str__( i ) :
    return str(i.name ) 

class Num:

  def rowStr( i ) :
    if( i.invalid ) :
      return (("%10s  %10s  %10s  %10s  %10s") % ( "-", "-","-","-","-" ))
    else :
      return (("%10.4f  %10.4f  %10.4f  %10.4f  %10.4f") % ( i.mu,  i.m2, i.sd(), i.min, i.max))

  def __init__( i ) :
    i.mu      = 0
    i.n       = 0
    i.m2      = 0
    i.max     = -sys.maxint - 1
    i.min     = sys.maxint
    i.invalid = False

  def add( i, x):
    if( i.invalid ) :
      return 

    try :
      x = float(x)
    except Exception:
      i.invalid = True
      return

    i.n += 1
    i.max = max( i.max, x )
    i.min = min( i.min, x )

    delta    = x - i.mu
    i.mu  += delta/i.n
    i.m2  += delta*(x - i.mu)
    return x 

  def norm( i, x ) :
    denom = i.max - i.min
    if( denom == 0 ) : return 0

    norm = x - i.min / denom
    return max( min ( norm, 1), 0 )

    
  def dist( i, a, b ) : 
    return abs(i.norm(b) - i.norm(a))

  def furthest ( i, x ) :
    return i.max if x <(i.max-i.min)/2 else i.min

  def sd( i ):
    return 0 if i.n <= 2 else (i.m2/(i.n - 1))**0.5


"""
    Sym Class

    Stores the symbols metadata. 

"""
class Sym():

  def rowStr( i ) :
    return (("%5.4f  %5s  %-20s") % ( i.ent(), str(i.most),  str(i.mode)))

  def __init__( i ):
     i.counts, i.most, i.mode, i.n = {},0,None,0

  def add(i,x):
    i.n += 1
    new = i.counts[x] = i.counts.get(x,0) + 1
    if new > i.most:
      i.most, i.mode = new,x
    return x

  def norm( i, x )     : return x
  def dist( i, x, y)   : return 0 if x == y else 1
  def furthest( i, x ) : return "_" + x

  def ent(i):
    tmp = 0
    for val in i.counts.values():
      p = float(val)/float(i.n)
      if p:
        tmp -= p*math.log(p,2)
    return tmp  

if __name__ == '__main__' :
  
  tab = CSVReader( sys.argv[1] ).table()
  print( tab.header )
  print( tab.data )
  print( "ROW 1 :",  tab[0] )
  print()
  print( "Furthest : ", tab.furthest(0) )
  print()
  print( *[ tab[x] for x in tab.furthest(0) ], sep="\n")
  print()
  print( "Closest : ", tab.closest(0) )
  print()
  print( *[ tab[x] for x in tab.closest(0) ], sep="\n")
  print()
  print( "ROW 2 :",  tab[1] )
  print()
  print( "Furthest : ", tab.furthest(1) )
  print()
  print( *[ tab[x] for x in tab.furthest(1) ], sep="\n")
  print()
  print( "Closest : ", tab.closest(1) )
  print()
  print( *[ tab[x] for x in tab.closest(1) ], sep="\n")

