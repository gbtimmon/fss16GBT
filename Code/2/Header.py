class Header:
  def __init__( self, cols ) : 
    self.obj = [ _Header(x) for x in cols ]

    
class _Header:
  def __init__( self, name) : 
    self.number = Num()
    self.symbol = Sym()
    self.name   = name

     
class Num:

  def __init__( self ) :
    self.mu   = 0
    self.n    = 0
    self.m2   = 0
    self.max  = sys.minint
    self.min  = sys.maxint

  def add( self, x):
    x = float(x)

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

  def sd(i):
    return 0 if self.n <= 2 else (self.m2/(self.n - 1))**0.5
from collections import defaultdict
from collections import OrderedDict

class Sym():

  def __init__( self ):
     self.counts = defaultdict(int)
     self.uniq   = {}
     self.most   = 0
     self.mode   = None
     self.n      = 0

  def add(self, x):
    self.n += 1
    self.counts[x] = self.counts[x] + 1

    if x not in self.uniq : self.uniq[x] = len(self.uniq) + 1
        
    
    if self.counts[x] > self.most:
      self.most = self.counts[x]
      self.mode = x

    return x

  def sub( self, x ):
    self.n -= 1
    self.counts[x] -= 1

    if x == self.mode:
      "wut?"
      self.most, self.mode = None,None

  def ent(i):
    tmp = 0
    for val in self.counts.values():
      p = val/self.n
      if p:
        tmp -= p*math.log(p,2)
    return tmp  

