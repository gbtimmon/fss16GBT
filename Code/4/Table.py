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
import random
import math
import sys
import re
sys.dont_write_bytecode = True

class cache():
  """
  TODO - FIX
  Broken -- needs to be fix but is currently commented out
  The cache seems to not work in objects. Need to debug
  """
  def __init__(i, func):
    i.func = func
    i.val  = None

  def __call__(i):
    if i.val is None : i.val = i.func()
    return i.val


class Vector : 
  """
  Vector class add a standard interface to data objects which are 
  wrappers for any list of data. Just as a sub set of a list returns a 
  new instance of list, any subset of vector wil return a new instance of 
  vector. Shouldnt be noticable slower than normal list operations. 
  """
  def __len__( i )           : return len( i.data ) 
  def __getitem__( i , x )   : return i.data[x]
  def __iter__( i )          : return i.data.__iter__()
  def __setitem__( i, x, y ) : i.data[x] = y
  def __str__( i )           : return i.data.__str__()
  def __repr__( i )          : return i.data.__repr__()
  def __copy__( i )          : return i.__class__(i) 
  def copy( i )              : return i.__copy__()

class CSVReader( ) : 

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
     i.data = [ x for x in data ]
     i.id   = Row.idGen = Row.idGen + 1

  def __str__( i ) : 
    return ("Row(" + str(i.id) + ") " + str(i.data) ) 
     

class Table(Vector):
  """
  Table is a Vector but it has a slightly altered behavior in that a subest of a table is 
  another table instance
  """ 
  idGen = 0

  def __init__( i, stream, noHeader=False, header=None, shallowCopy=True ) : 
    i.rowCount = 0 
    i.id       = Table.idGen = Table.idGen + 1 
    if header is None and not noHeader : 
      i.header = Header( stream.__iter__().next() )
    elif not noHeader : 
      i.header = Header( header )
    else :
      i.header = None
      
    i.data = []

    for x in stream : 
      i.rowCount += 1

      if i.header is None :
        i.header = Header( range(len(x)) )

      i.header.add(x)

      if shallowCopy :
        i.data.append(x)
      else :
        i.data.append( x.copy() )

  def __getitem__( i, x ) : 
    if( isinstance(x, int) ):
       return Vector.__getitem__(i, x) 
    if ( isinstance( x, tuple ) or isinstance( x, list ) ) : 
       return Table( [ i[y] for y in x ], header=i.colNames() )

  def copy( i ) :
     return i.__class__( i, header=i.header, shallowCopy=True )
  def deepcopy( i ) :
     return i.__class__( i, header=i.header, shallowCopy=False )

  def furthesti( i, x ) : 
    arr = i.disti(x)
    return [ i for i,j in enumerate(arr) if j == max(arr) ] 

  def furthest( i, x ) :
    return i[ i.furthesti(x) ]

  def closesti( i, x ) : 
    arr = i.disti(x)
    arr_min = min( [ k for k in arr if k > 0 ] )
    return [ j for j,k in enumerate(arr) if k == arr_min ]
  
  def closest( i, x ) :
    return i[ i.closesti(x) ]
 
  def sample( i, n, percent=False, shallowCopy=True ) :
    if percent :
      if n > 1 or n < 0 : 
        raise TypeError("percent out of bounds")
      n = len(i) * n
    return Table( random.sample(i, n), header=i.colNames(), shallowCopy=shallowCopy )

  def disti( i, a, b=None, f=2 ) :

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
         
         v1 = a[ col ]
         v2 = b[ col ]

         if( v1 is None and v2 is None ): continue
         if( v1 is None ) : v1 = hd.furthest(v2)
         if( v2 is None ) : v2 = hd.furthest(v1)
         s += hd.dist( v1, v2) ** f

      return (( float(s) ** (1.0/float(f)))/(float(n)**(1.0/float(f))))
    "END HELPER FUNCTION"

    ar = a if isinstance(a, Row ) else i[a]
    if b is not None :
      br = b if isinstance( b, Row ) else i[b]
      return _dist(i, ar, b=br)

    return [ _dist(i, ar, i[x]) for x in range(len(i))]

  def dist( i, x ) : 
    return i[ i.disti( x ) ]

  def colNames( i ) :
    return [str(x.name) for x in i.header ]

  def dataStr( i ) :
    return "\n".join([ str(x) for x in i.data])

  def __str__( i ) : 
    return (
      "Table(" + str(i.id) + ")\n" +
      "  Row count : "+str(i.rowCount) + "\n\n"+
      "\n".join([ str(x) for x in i.header ])
    )
    

class Header(Vector) : 
  def __init__( i, col ) : 
    i.data = [ _Header(col[x], x) for x in xrange(len(col)) ]

  def add( i, row ) :
    for x, y in zip(i.data, row) : 
       x.add(y)

  def __str__( i ) : 
    return str([ str(x) for x in i.data ])
 

class _Header:

  def isDep( i )      : return i.dep
  def norm( i, x )    : return i.stat.norm( x )
  def dist( i, x, y ) : return i.stat.dist( x, y)
  def furthest( i, x ): return i.stat.furthest( x ) 

  def __init__ ( i, name, pos) : 
    i.pos  = pos
    i.dep  = True if( name[0] == "=" ) else False
    i.stat = None
    i.name = re.sub(r'[=><\-_]', '', name.strip())

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
    return "Pos:%3s Name:%-15s Dep:%5s %s" % ( str(i.pos), str(i.name) ,str(i.dep), str(i.stat))

class Num:

  def __init__( i ) :
    i.mu      = 0
    i.n       = 0
    i.m2      = 0
    i.max     = -sys.maxint - 1
    i.min     = sys.maxint

  def __str__( i ) : 
    return "NUM mu:%s n:%s m2:%s max:%s min:%s" %( str(i.mu), str(i.n), str(i.m2), str(i.max), str(i.min))

  def add( i, x):
    x = float(x)

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

  def __str__( i ) :
    return (("SYM ENT : %5.4f  MOST : %5s  MODE : %-20s") % ( i.ent(), str(i.most),  str(i.mode)))

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

