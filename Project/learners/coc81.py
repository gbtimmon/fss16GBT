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

table="../data/coc81.arff"

t = Reader( table , sep=" " ).table()
#data = np.array( t.data ) 
data=t.data
#print data[0]
# embedded=1, semidetached=2, organic=3
# vl=0, l=1, n=2, h=3,vh=4, xh=5
xtrain,ytrain=[],[]
for i in range(len(data)):
	#print i
	xtrain.append(data[i][1:23])
	ytrain.append([data[i][23]])#, data[i][len(data[0])-1]])
	if(xtrain[i][0]=="'embedded'"):
		xtrain[i][0]=1
	elif(xtrain[i][0]=="'semidetached'"):
		xtrain[i][0]=2
	elif(xtrain[i][0]=="'organic'"):
		xtrain[i][0]=3
	for j in range(22):
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

#print xtrain[0]
xtrain=np.array(xtrain).astype(float)
ytrain=np.array(ytrain).astype(float)
runmodel(xtrain,ytrain)