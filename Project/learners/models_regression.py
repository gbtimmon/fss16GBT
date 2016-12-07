import numpy as np
from sklearn import svm
from sklearn import preprocessing
from sklearn.linear_model import *
from sklearn.cross_validation import cross_val_score
from basic_cocomo import *

def runmodel(xtrain,ytrain):
	methods = [svm.SVR(),Lasso()]
	for method in methods:
	    searchCV = method
	    print( "Error rates: "+str(cross_val_score(searchCV, xtrain, ytrain, cv=5, score="recall_weigthed")) ) 

def runcocomo(xtrain):
	l=len(xtrain[0])
	for i in range(len(xtrain)):
		cocomo_months(0, float(xtrain[i][l-1]))
		#print ytrain[i]
