from collections import defaultdict
class Sym():

  def __init__(self, attr_name=None):
     self.counts = defaultdict(int)
     self.most   = 0
     self.mode   = None
     self.n      = 0

  def add(self, x):
    self.n += 1
    self.counts[x] = self.counts[x] + 1
    
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
