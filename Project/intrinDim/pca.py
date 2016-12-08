import numpy as np
import sys 
import matplotlib
import matplotlib.pyplot as plt

def pca( A, threshold, plot=False ) :

#Make a random array and then make it positive-definite
  A = np.array( A ) 
  A = np.asmatrix(A.T) * np.asmatrix(A)
  U, S, V = np.linalg.svd(A) 
  eigvals = S / np.cumsum(S)[-1]

  print( np.where( eigvals > threshold )[0].size)

  if( plot ) : 
    fig, ax = plt.subplots() 
    sing_vals = np.arange(1,eigvals.size + 1)
    plt.bar(sing_vals, eigvals)
    plt.title('Scree Plot')
    plt.xlabel('Principal Component')
    plt.ylabel('Eigenvalue')
    plt.axhline(y=0.002, xmin=0, xmax=100, hold=None)
    plt.axhline(y=0.003, xmin=0, xmax=100, hold=None)
    plt.axhline(y=0.004, xmin=0, xmax=100, hold=None)
    ax.set_yscale( 'log', basey=2 ) 
    #I don't like the default legend so I typically make mine like below, e.g.
    #with smaller fonts and a bit transparent so I do not cover up data, and make
    #it moveable by the viewer in case upper-right is a bad place for it 
    leg = plt.legend(['Eigenvalues from SVD'], loc='best', borderpad=0.3, 
                   shadow=False, prop=matplotlib.font_manager.FontProperties(size='small'),
                   markerscale=0.4)
    leg.get_frame().set_alpha(0.4)
    leg.draggable(state=True)
    plt.show()

  return np.cumsum( eigvals ) 
