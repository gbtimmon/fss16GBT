#!python
from __future__ import print_function

import sys 
from Sym import Sym

__author__='greg timmons'

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def repString( sym, x ) :
   return  str(sym.uniq[x]) + ":" + str(x)  

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
   
   # 1.) load all of lines that are non empty
   # 2.)load all of the attributes. 
   # 3.)grab all the none @ lines, these should be data. 
   
   train_inf = [ x for x in map( str.strip, open(trainFile, "r").readlines() ) if len(x) > 0]
   train_atr = [ x[11:].split(" ", 1) for x in train_inf if x[0:10] == "@attribute" ]
   train_dat = [ x.split(",") for x in train_inf if x[0] != "@" ]
  
   test_inf = [ x for x in map( str.strip, open(testFile, "r").readlines() ) if len(x) > 0]
   test_atr = [ x[11:].split(" ", 1) for x in test_inf if x[0:10] == "@attribute" ]
   test_dat = [ x.split(",") for x in test_inf if x[0] != "@" ]

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
