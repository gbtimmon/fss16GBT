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
from models_classify import *

table="../data/iris.csv"

t = Reader( table, sep="," ).table()
data = np.array( t.data ) 

#dataset= arff.load(open('../data/nasa93.arff'))
#data = np.array(dataset['data'])


xtrain,ytrain=[],[]
for i in range(len(data)):
	xtrain.append(data[i][0:4])
	ytrain.append([data[i][4]])
print
#xtrain=np.array(xtrain).astype(float)
xtrain=np.asarray(xtrain, dtype=float)
#print xtrain[0][0]
ytrain=np.array(ytrain).ravel()
runmodel(xtrain,ytrain)
#print xtrain[0]
#print ytrain[0]
