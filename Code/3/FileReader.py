import os
def factory(  params ) : 

  fileName = params["fileName"]

  def checkParams( params, validParams ) :
    for x in params.keys() : 
      if( x not in validParams ) : 
        raise ValueError( str(x) + " is and invalid parameter for file type " + os.path.splitext(fileName)[1] )

  if( fileName.lower().endswith(".csv") ) :
    checkParams( params, ["fileName", "sep", "missing"] )
    return _CSVReader(params).__iter__()

  else :
    return None


   
class _CSVReader : 

  def __init__ (self, params) : 
    
    import sys
    self.fileName   = params["fileName"]
    self.sep        = params["sep"] if(params["sep"] ) else ","
    self.missing    = params["missing"] if(params["missing"] ) else None
    self.curLine    = 0
    self.fileHandle = open( self.fileName, "r" ) if( self.fileName != None ) else sys.stdin

   
  def __iter__(self):
    for line in self.fileHandle :
      line = line.strip()
      if( len(line) == 0 ) : continue
      if( line[0] == "%")  : continue
      yield map( self.wrangle, line.split( self.sep ) )

  def wrangle(self, inv ) :

    if( int == self.missing ) : return None

    try  : return int(inv)
    except Exception : pass
 
    try  : return float(inv)
    except Exception : pass

    inv = inv.strip()
    return str(inv)
  
     
