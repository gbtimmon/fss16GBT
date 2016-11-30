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

table="../data/wine.csv"

t = Reader( table, sep="," ).table()
data = np.array( t.data ) 


#dataset= arff.load(open('../data/nasa93.arff'))
#data = np.array(dataset['data'])
# vl=0, l=1, n=2, h=3,vh=4, xh=5
#print data[0]
xtrain,ytrain=[],[]
for i in range(len(data)):
	xtrain.append(data[i][0:13])
	ytrain.append([data[i][13]])#, data[i][len(data[0])-1]])

print
xtrain=np.array(xtrain).astype(float)
ytrain=np.array(ytrain).astype(float)
runmodel(xtrain,ytrain)
#print xtrain[0]
#print ytrain[0]