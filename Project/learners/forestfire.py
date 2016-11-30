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

table="../data/forestfire.csv"

t = Reader( table, sep="," ).table()
data = np.array( t.data ) 

#dataset= arff.load(open('../data/nasa93.arff'))
#data = np.array(dataset['data'])
# vl=0, l=1, n=2, h=3,vh=4, xh=5
print data[0]
xtrain,ytrain=[],[]
for i in range(len(data)):
	xtrain.append(data[i][0:12])
	ytrain.append([data[i][12]])#, data[i][len(data[0])-1]])
	mon=xtrain[i][2]
	if(mon=='jan'):
		mon= 1.0
	elif(mon=='feb'):
		mon= 2.0
	elif(mon=='mar'):
		mon= 3.0
	elif(mon=='apr'):
		mon= 4.0
	elif(mon=='may'):
		mon= 5.0
	elif(mon=='jun'):
		mon= 6.0
	elif(mon=='jul'):
		mon= 7.0
	elif(mon=='aug'):
		mon=  8.0
	elif(mon=='sep'):
		mon= 9.0
	elif(mon=='oct'):
		mon=  10.0
	elif(mon=='nov'):
		mon= 11.0
	elif(mon=='dec'):
		mon= 12.0
	xtrain[i][2]=mon

	day=xtrain[i][3]
	if(day=='mon'):
		day= 1.0
	elif(day=='tue'):
		day= 2.0
	elif(day=='wed'):
		day=  3.0
	elif(day=='thu'):
		day=  4.0
	elif(day=='fri'):
		day=  5.0
	elif(day=='sat'):
		day=  6.0
	elif(day=='sun'):
		day=  7.0
	xtrain[i][3]=day	
	
print
xtrain=np.array(xtrain).astype(float)
ytrain=np.array(ytrain).astype(float)
runmodel(xtrain,ytrain)
#print xtrain[0]
#print ytrain[0]
