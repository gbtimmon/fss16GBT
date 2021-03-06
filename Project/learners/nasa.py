import arff, numpy as np
import csv
import sys
import numpy as np
from sklearn import svm
from sklearn import preprocessing
from sklearn.linear_model import *
from sklearn.model_selection import cross_val_score
from basic_cocomo import *
from Table        import Table, Reader 
from models_regression import *

table="../data/nasa93.arff"

t = Reader( table, ignoreCols=(0,25,26), sep="," ).table()
data = np.array( t.data ) 


#dataset= arff.load(open('../data/nasa93.arff'))
#data = np.array(dataset['data'])
# vl=0, l=1, n=2, h=3,vh=4, xh=5
#print data[0]
xtrain,ytrain=[],[]
for i in range(len(data)):
	xtrain.append(data[i][0:23])
	ytrain.append([data[i][23]])#, data[i][len(data[0])-1]])
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
print
xtrain=np.array(xtrain).astype(float)
ytrain=np.array(ytrain).astype(float)
runmodel(xtrain,ytrain)
#print xtrain[0]
#print ytrain[0]