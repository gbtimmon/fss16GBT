import arff, numpy as np
import csv
import sys
import numpy as np
from sklearn import svm
from sklearn import preprocessing
from sklearn.linear_model import *
from basic_cocomo import *


dataset= arff.load(open('coc81.arff'))
data = np.array(dataset['data'])
# embedded=1, semidetached=2, organic=3
print data[0]
xtrain,ytrain=[],[]
for i in range(len(data)):
	xtrain.append(data[i][1:18])
	ytrain.append([data[i][18]])#, data[i][len(data[0])-1]])
	if(xtrain[i][0]=='embedded'):
		xtrain[i][0]=1
	elif(xtrain[i][0]=='semidetached'):
		xtrain[i][0]=2
	elif(xtrain[i][0]=='organic'):
		xtrain[i][0]=3


methods = [svm.SVR()]
for method in methods:
    searchCV = method
    searchCV.fit(xtrain, ytrain)
    print
    print str(searchCV.predict(xtrain[1]))
print
#print xtrain[0]
print ytrain[0]
l=len(xtrain[0])
for i in range(len(xtrain)):
	print str(cocomo_months(xtrain[i][0],float(xtrain[i][l-1])))+ " months in cocomo"

