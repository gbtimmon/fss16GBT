#!python

__author__='greg timmons'

import sys 
from Sym import Sym

class Attr() : 
    def __init__( self, name, atype ) : 
        self.name = name
       

def main( ) :

   attr_count = 0
   pred = Sym()
   

   # load all of lines that are none empty
   inf = [ x for x in map( str.strip, sys.stdin ) if len(x) > 0]

   # load all of the attributes. 
   atr = [ x[11:].split(" ", 1) for x in inf if x[0:10] == "@attribute" ]

   #grab all the none @ lines, these should be data. 
   dat = [ x.split(",") for x in inf if x[0] != "@" ]
  
   attrIndex = len( atr ) - 1

   map( pred.add, [ x[attrIndex] for x in dat ] ) 

   print pred.mode   
       


if __name__ == '__main__' : 
   main()
