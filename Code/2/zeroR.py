#!python
from __future__ import print_function

import sys 
from Sym import Sym

__author__='greg timmons'

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def repString( sym, x ) :
   return  str(sym.uniq[x]) + ":" + str(x)  

def loadFile( ff ) :

   # 1.) load all of lines that are non empty
   # 2.)load all of the attributes. 
   # 3.)grab all the none @ lines, these should be data. 

   inf = [ x for x in map( str.strip, open(ff, "r").readlines() ) if len(x) > 0]
   atr = [ x[11:].split(" ", 1) for x in inf if x[0:10] == "@attribute" ]
   dat = [ x.split(",") for x in inf if x[0] != "@" ]
 
   return atr, dat


def main( ) :

   trainFile = ""
   testFile  = ""

   if(len(sys.argv) == 2) : 
      trainFile = testFile = sys.argv[1]

   elif( len(sys.argv) == 3 ) :
      trainFile = sys.argv[1]
      testFile  = sys.argv[2]
  
   else :
      eprint( "Improper number of arguments passed : " + sys.argv )
      sys.exit(1)



   attr_count = 0
   pred = Sym()
   
   train_atr, train_dat = loadFile( trainFile )  
   test_atr, test_dat   = loadFile( testFile )  
  

   # Generate a symbol class for the prediction attribute so that we can find the mode
   # and assign it as the prediction. 
   attrIndex = len( train_atr ) - 1
   map( pred.add, [ x[attrIndex] for x in train_dat ] ) 
   prediction = pred.mode

   # output the testing result on the testing data. 

   print("=== Predictions on test data ===")
   print("")
   print(" inst#     actual  predicted error prediction")
   ln = 1
   for line in test_dat:
       print ( "%6s %10s %10s %07s" % ( 
             ln,
             repString( pred, line[attrIndex]),
             repString( pred, pred.mode),
             "1" if line[attrIndex] == pred.mode else "0"   
       ))
       ln += 1

if __name__ == '__main__' : 
   main()
