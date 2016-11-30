import arff, numpy as np
import csv
import sys
import numpy as np
from sklearn import svm
from sklearn import preprocessing
from sklearn.linear_model import *
from basic_cocomo import *

dataset= arff.load(open('nasa93.arff'))
data = np.array(dataset['data'])
# vl=0, l=1, n=2, h=3,vh=4, xh=5
print data[0]
xtrain,ytrain=[],[]
for i in range(len(data)):
	xtrain.append(data[i][1:24])
	ytrain.append([data[i][24]])#, data[i][len(data[0])-1]])
	for j in range(23):
		if(xtrain[i][j]=='vl'):
			xtrain[i][j]=0.0
		elif(xtrain[i][j]=='l'):
			xtrain[i][j]=1.0
		elif(xtrain[i][j]=='n'):
			xtrain[i][j]=2.0
		elif(xtrain[i][j]=='h'):
			xtrain[i][j]=3.0
		elif(xtrain[i][j]=='vh'):
			xtrain[i][j]=4.0
		elif(xtrain[i][j]=='xh'):
			xtrain[i][j]=5.0


methods = [svm.SVR()]
for method in methods:
    searchCV = method
    print "Fitting..."
    searchCV.fit(xtrain, ytrain)
    print str(searchCV.predict(xtrain[0]))
#print xtrain[0]
#print ytrain[0]

l=len(xtrain[0])
for i in range(len(xtrain)):
	print str(cocomo_person(0, float(xtrain[i][l-1])))+"person months compared to:"
	print ytrain[i]