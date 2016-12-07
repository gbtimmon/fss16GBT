#!python
import sys 
from random import uniform 
import math

class MonteCarloSim : 

  " MonteCarloSim             " 
  "---------------------------"                       
  " Given an input model,     "
  " will output sample points "

  @staticmethod
  def scaffer() : return MonteCarloSim( *_schaffer )
  def osyczka() : return MonteCarloSim( *_osyczka )
  def kursawe() : return MonteCarloSim( *_kursawe )

  def __init__(self,name, *decl, **kwargs):
    self.name = name
    self.v    = [ x for x in decl if isinstance( x, Variable ) ]
    self.c    = [ x for x in decl if isinstance( x, Constraint ) ]
    self.f    = [ x for x in decl if isinstance( x, Function ) ]

  def header( self ) :
    return [ x.name for x in self.v] + [ x.name for x in self.f]

  def generate( self, k: int ) :
    samples = 0 
    while samples < k : 
      var = [ x() for x in self.v ]

      if any( [ not c( var ) for c in self.c ] ) :
        continue 

      out = [ f( var ) for f in self.f ]
      
      samples += 1
      yield( var + out ) 

class Variable :
  def __init__( self, name, minVal, maxVal ) : 
    self.name = name
    self.min  = minVal
    self.max  = maxVal
  def __call__( self ) :
    return uniform( self.min, self.max )

class Constraint:
  def __init__( self, name, validator ) : 
    self.name      = name
    self.validator = validator
  def __call__( self, inputs ) : 
    return self.validator( inputs ) 

class Function :
  def __init__( self, name, function ) : 
    self.name     = name 
    self.function = function
  def __call__( self, inputs ) :
   return self.function( inputs ) 
  
_schaffer = [
    "Schaffer", 
    Variable("x",-10**5,10**5),
    Function("f1", lambda x: x[0]**2),  
    Function("f2", lambda x: (x[0]-2)**2),
]

_osyczka = [
    "Osyczka",
    Variable("x1",0,10),
    Variable("x2",0,10),
    Variable("x3",1,5),
    Variable("x4",0,6),
    Variable("x5",1,5),
    Variable("x6",0,10),
    Function("f1", lambda x: -1*(25*(x[0]-2)**2 + (x[1]-2)**2 + ((x[2]-1)**2)*((x[3]-4)**2) + (x[4] - 1)**2)),
    Function("f2", lambda x: sum([i**2 for i in x])),
    Constraint( "c1", lambda x: 0 <= (x[0] + x[1] - 2) ),
    Constraint( "c2", lambda x: 0 <= (6 - x[0] - x[1]) ),
    Constraint( "c3", lambda x: 0 <= (2 - x[1] + x[0]) ), 
    Constraint( "c4", lambda x: 0 <= (2 - x[0] + 3*x[1]) ),
    Constraint( "c5", lambda x: 0 <= (4 - (x[2] - 3)**2 - x[3]) ),  
    Constraint( "c6", lambda x: 0 <= ((x[4] - 3)**3 + x[5] - 4) ) 
]

_kursawe = [
    "Kursawe",
    Variable("x1",-5,5),
    Variable("x2",-5,5),
    Variable("x3",-5,5),
    Function("f1", lambda dec: sum([(-10)*(math.e**(-0.2*((dec[i]**2 + dec[i+1]**2)**0.5))) for i in [0,1]])),
    Function("f2", lambda dec: sum([abs(x)**0.8 + 5*math.sin(x)**3 for x in dec]))
]


if __name__ == '__main__' : 

  models = [ _schaffer, _osyczka, _kursawe ]
  if len( sys.argv ) != 3 : 
    print( "Give me moteCarloSim <modelNum> <ObsCount>" )
    exit(1)

  m =  MonteCarloSim( *models[ int(sys.argv[1]) - 1 ] )

  print( *m.header(), sep=", " )
  for obs in m.generate( int( sys.argv[2] ) ): 
    print( *["%3.2f"%x for x in obs], sep=", ")

  





