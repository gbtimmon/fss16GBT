import numpy as np
from sklearn import svm
from sklearn import preprocessing
from sklearn.linear_model import *
from sklearn.model_selection import cross_val_score
from basic_cocomo import *

def runmodel(xtrain,ytrain):
	methods = [svm.SVR(),Lasso()]
	for method in methods:
	    searchCV = method
	    #print "Fitting..."
	    searchCV.fit(xtrain, ytrain)
	    print
	    #print str(searchCV.predict(xtrain[0]))
	    print "Error rates: "+str(cross_val_score(searchCV, xtrain, ytrain))
	    #runcocomo(xtrain)

def runcocomo(xtrain):
	l=len(xtrain[0])
	for i in range(len(xtrain)):
		cocomo_months(0, float(xtrain[i][l-1]))
		#print ytrain[i]