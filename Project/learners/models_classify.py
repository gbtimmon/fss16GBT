import numpy as np
from sklearn import svm
from sklearn import preprocessing
from sklearn.linear_model import *
from sklearn.cross_validation import cross_val_score
from basic_cocomo import *

def runmodel(xtrain,ytrain):
	methods = [svm.SVC()]
	xtrain=np.array(xtrain).astype(float)
	ytrain=np.array(ytrain).astype(str)
	for method in methods:
	    searchCV = method
	    #print "Fitting..."
	    searchCV.fit(xtrain, ytrain)
	    print
	    #print str(searchCV.predict(xtrain[0]))
	    
	    print( "Error rates: "+str(cross_val_score(searchCV, xtrain, ytrain, scoring="recall_weighted")))
