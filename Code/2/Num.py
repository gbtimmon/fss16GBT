class Num:

  def __init__( self, attr_name=None) :
    self.name = attr_name
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
