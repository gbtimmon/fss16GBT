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

table="../data/cocomosdr.arff"

t = Reader( table, ignoreCols=(0,25,26), sep="," ).table()
data = np.array( t.data ) 
#data=t.data
#dataset= arff.load(open('cocomosdr.arff'))
#data = np.array(dataset['data'])
# vl=0, l=1, n=2, h=3,vh=4, xh=5
#Low,'Very Low',High,'Extra High','Very High',Nominal}
#print data[0]
xtrain,ytrain=[],[]
for i in range(len(data)):
	xtrain.append(data[i][0:23])
	ytrain.append([data[i][23]])#, data[i][len(data[0])-1]])
	for j in range(23):
		if(xtrain[i][j]=="'Very Low'"):
			xtrain[i][j]=0.0
		elif(xtrain[i][j]=="Low"):
			xtrain[i][j]=1.0
		elif(xtrain[i][j]=="Nominal"):
			xtrain[i][j]=2.0
		elif(xtrain[i][j]=="High"):
			xtrain[i][j]=3.0
		elif(xtrain[i][j]=="'Very High'"):
			xtrain[i][j]=4.0
		elif(xtrain[i][j]=="'Extra High'"):
			xtrain[i][j]=5.0

#print xtrain[0]
xtrain=np.array(xtrain).astype(float)
ytrain=np.array(ytrain).astype(float)
runmodel(xtrain,ytrain)