from __future__ import division
import sys
sys.path.insert(0, "..")
from Table import Row

r1 = Row([1,2,3,4,5,6])
r2 = Row([6,5,4,3,2,1])

print (r1)
print (r2)

print (r1.blend(r2))
for i in xrange(11) :
   print (r1.blend(r2, rate=(i/10)))

