def factory( fileName ) : 
  if( fileName.lower().endswith(".csv") ) :
    return _CSVReader(fileName=fileName).__iter__()
  else :
    return None

def wrangle( inv ) :
   try  : return int(inv)
   except Exception : pass

   try  : return float(inv)
   except Exception : pass

   inv = inv.strip()
   return str(inv)


   
class _CSVReader : 

  def __init__ (self, fileName=None, sep=",", hasHeader=True ) : 
    import sys
    self.sep    = sep
    self.curLine  = 0
    self.hasHeader  = hasHeader 
    self.fileName   = fileName
    self.fileHandle = open( fileName, "r" ) if( fileName != None ) else sys.stdin

   
  def __iter__(self):
    for line in self.fileHandle :
      line = line.strip()
      if( len(line) == 0 ) : continue
      if( line[0] == "%")  : continue
      yield map( wrangle, line.split( self.sep ) )

  
  
