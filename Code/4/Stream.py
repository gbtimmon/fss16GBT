"""
  Auto Flush Stream
  -------------------------------------------------------
  adds a couple control functions to a Stream to make for 
  prettier outputs. 

  

"""
class Unbuffered(object): 

  def __init__(self, stream):
    self.stream = stream
    self.indent = 0
    stream = self 

  def write(self, data):
    self.stream.write((" " * self.indent) + data)
    self.stream.flush()

  def setIndent( self, x ) : 
    self.indent = x 

  def getRawStream( self ) : 
    return self.stream

  def __getattr__(self, attr):
    return getattr(self.stream, attr)
