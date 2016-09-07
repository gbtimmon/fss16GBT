#!python

__author__='greg timmons'

import sys 

class Attr() : 
    def __init__( self, name, atype ) : 
        self.name = name
       

def main( ) :

   

   # load all of the attributes
   for line in map( str.strip, sys.stdin ) :
      
      if( len(line) < 1 ) :
         continue

      line = line.split()

      if(line[0] == "@attribute" ) :
         print "Name " + line          

         
       


if __name__ == '__main__' : 
   main()
