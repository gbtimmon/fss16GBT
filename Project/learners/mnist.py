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

table="../data/mnist_pca_8or9.csv"

t = Reader( table, sep="," ).table().oneHot()
data = np.array( t.data ) 

#dataset= arff.load(open('../data/nasa93.arff'))
#data = np.array(dataset['data'])
# vl=0, l=1, n=2, h=3,vh=4, xh=5
#print data[0]
xtrain,ytrain=[],[]
for i in range(len(data)):
	xtrain.append(data[i][0:10])
	ytrain.append([data[i][10:11]])
print
xtrain=np.array(xtrain).astype(str)
ytrain=np.array(ytrain).ravel().astype(str)
runmodel(xtrain,ytrain)
#print xtrain[0]
#print ytrain[0]
