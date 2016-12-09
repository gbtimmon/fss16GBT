#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np

def intrinsic_dimension(X, kmin=6, kmax=12, estimator='levina' ):

    n = X.shape[0]
    X = X.copy().astype(float)
    X = X[np.lexsort(np.fliplr(X).T)]
       
    # Standardization
    X -= X.mean(axis=0) 
    X /= X.std(axis=0) + 1e-7 
      
    # Compute matrix of log nearest neighbor distances
    X2 = (X**2).sum(1)
    distance = X2.reshape(-1, 1) + X2 - 2*np.dot(X, X.T) #2x br.cast
    distance.sort(1)
    distance[distance <= 0] = 10e-7
    knn = .5 * np.log(distance[:, 1:kmax+1])
   
    # Compute the ML estimate
    S = np.cumsum(knn, 1)
    K = np.arange(kmin, kmax+1) 
    dhat = -( K - 2 ) / ( S[ : , kmin-1 : kmax] - knn[ : , kmin - 1 : kmax ] * K )

    return dhat.mean()
    
