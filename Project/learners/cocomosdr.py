import arff, numpy as np
import csv
import sys
import numpy as np
from sklearn import svm
from sklearn import preprocessing
from basic_cocomo import *
from sklearn.linear_model import *


dataset= arff.load(open('cocomosdr.arff'))
data = np.array(dataset['data'])
# vl=0, l=1, n=2, h=3,vh=4, xh=5
#Low,'Very Low',High,'Extra High','Very High',Nominal}
print data[0]
xtrain,ytrain=[],[]
for i in range(len(data)):
	xtrain.append(data[i][1:24])
	ytrain.append([data[i][24]])#, data[i][len(data[0])-1]])
	for j in range(22):
		if(xtrain[i][j]=='Very Low'):
			xtrain[i][j]=0.0
		elif(xtrain[i][j]=='Low'):
			xtrain[i][j]=1.0
		elif(xtrain[i][j]=='Nominal'):
			xtrain[i][j]=2.0
		elif(xtrain[i][j]=='High'):
			xtrain[i][j]=3.0
		elif(xtrain[i][j]=='Very High'):
			xtrain[i][j]=4.0
		elif(xtrain[i][j]=='Extra High'):
			xtrain[i][j]=5.0


methods = [svm.SVR()]
for method in methods:
    searchCV = method
    searchCV.fit(xtrain, ytrain)
    print str(searchCV.predict(xtrain[1]))
#print xtrain[1]
#print ytrain[1]
l=len(xtrain[0])
for i in range(len(xtrain)):
	print str(cocomo_months(0,float(xtrain[i][l-1])/1000.0))+" months compared to:"
	print ytrain[i]