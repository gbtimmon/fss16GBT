from __future__ import print_function
import sys
"""
  eXtended Stream
  -------------------------------------------------------
  adds a couple control functions to a Stream to make for 
  prettier outputs. 

  Disclaimer : 
  This is experimental ... 
  Its probably a bad idea, but I though it was fun ... Sorry ;).

"""

COLOR_MAP = {
   "r": "31", #red
   "g": "32", #green
   "y": "33", #yellow
   "b": "34", #blue
   "m": "35", #magenta
   "c": "36", #cyan
   "w": "37"  #white 
}

def cstr( arg, clr ) : 
  return "\033[" + COLOR_MAP[clr] + "m" + str(arg) + "\033[0m"

class XStream(object): 

  def __init__(self, 
      stream, 
      indent       = 0,     # set default indentation
      auto_flush   = False, # set auto flushing policy
      color        = "w",   # set default color
      dont_destroy = False  # indicate if I should replace the stream object. 
    ):

    self.stream     = stream
    self.auto_flush = auto_flush
    self.indent     = indent
    self.color      = color

    if not dont_destroy :
      stream = self 

  def __call__( self, *args, **kwargs ) :
    self.write(*args, **kwargs )
    return self

  def nl ( self ) : 
    self.write("\n");
    return self

  def write(self, 
    arg, 
    color=None,   # color to overide default
    flush=False  # flush policy to override default
  ):

    clr = color if color is not None else self.color
    self.stream.write(cstr((" " * self.indent) +  str(arg) ,clr)) #OMG what a hack :/
    return self



  """
     Getters and Setters 
  """
  def setAutoFlush( self, x ) : 
    self.auto_flush = x 
    return self

  def setIndent( self, x )    : 
    self.indent = x 
    return self

  def getRawStream( self )    : return self.stream
  def __getattr__(self, attr) : return getattr(self.stream, attr)

  def setColor( self, x ) : 
    self.color = COLOR_MAP[x]
    self._changeColor( self.color ) 
    return self
