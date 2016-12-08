#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np

def intrinsic_dimension(X, k1=6, k2=12, 
                        estimator='levina', metric='vector', 
                        trafo='var', mem_threshold=5000):

    n = X.shape[0]
    if estimator not in ['levina', 'mackay']:
        raise ValueError("Parameter 'estimator' must be 'levina' or 'mackay'.")
    if k1 < 1 or k2 < k1 or k2 >= n:
        raise ValueError("Invalid neighborhood: Please make sure that "
                         "0 < k1 <= k2 < n. (Got k1={} and k2={}).".
                         format(k1, k2))
    X = X.copy().astype(float)
        
    X = X[np.lexsort(np.fliplr(X).T)]
        
    if trafo is None:
        pass
    elif trafo == 'var':
        X -= X.mean(axis=0) # broadcast
        X /= X.var(axis=0) + 1e-7 # broadcast
    elif trafo == 'std':
        # Standardization
        X -= X.mean(axis=0) # broadcast
        X /= X.std(axis=0) + 1e-7 # broadcast
    else:
        raise ValueError("Transformation must be None, 'std', or 'var'.")
      
    # Compute matrix of log nearest neighbor distances
    X2 = (X**2).sum(1)
        
    if n <= mem_threshold: # speed-memory trade-off
        distance = X2.reshape(-1, 1) + X2 - 2*np.dot(X, X.T) #2x br.cast
        distance.sort(1)
        # Replace invalid values with a small number
        distance[distance <= 0] = 10e-7
        knnmatrix = .5 * np.log(distance[:, 1:k2+1])
    else:
        knnmatrix = np.zeros((n, k2))
        for i in range(n):
            distance = np.sort(X2[i] + X2 - 2 * np.dot(X, X[i, :]))
            # Replace invalid values with a small number
            distance[distance <= 0] = 10e-7
            knnmatrix[i, :] = .5 * np.log(distance[1:k2+1])
   
    # Compute the ML estimate
    S = np.cumsum(knnmatrix, 1)
    indexk = np.arange(k1, k2+1) # broadcasted afterwards
    dhat = -(indexk - 2) / (S[:, k1-1:k2] - knnmatrix[:, k1-1:k2] * indexk)

    if estimator == 'levina':  
        # Average over estimates and over values of k
        no_dims = dhat.mean()
    if estimator == 'mackay':
        # Average over inverses
        dhat **= -1
        dhat_k = dhat.mean(0)
        no_dims = (dhat_k ** -1).mean()
    return no_dims
    
