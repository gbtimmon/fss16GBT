from __future__ import division
import sys
from O import o 

class ResultSet(o) : 
  def __init__( self, trn, tst, results ) :
    super( ResultSet, self).__init__()
    self.train    = trn
    self.test     = tst
    self.values   = {}
    self.result   = []
    self.sformat  = "{:5} " * 4
    self.metric   = o(TP=0, TN=0, FP=0, FN=0)
    self._eps     = 10e-40

    cur_val  = 1
    for i, tup in enumerate(results) :
      ex = tuple( self.test.set.getDependentValues( tup[0] ) )
      pd = tuple( self.test.set.getDependentValues( tup[1] ) )
      rs = "1" if ex == pd else "0"
 
      for it in [ex, pd] :
        if it not in self.values :
          n = o()
          n.id = cur_val
          n.count_exp = 0     
          n.count_prd = 0
          self.values[it] = n
          cur_val += 1
 
      self.values[ex].count_exp += 1
      self.values[pd].count_prd += 1
      self.result.append( o(row_num=i, expected=ex, predicted=pd, result=rs ) ) 

    self.minority = min([(k,v) for k,v in self.values.iteritems() ], key=lambda x: x[1].count_exp )[0]
    
    for row in self.result : 
      if row.expected == self.minority and row.predicted == self.minority : self.metric.TP += 1
      if row.expected == self.minority and row.predicted != self.minority : self.metric.FN += 1
      if row.expected != self.minority and row.predicted == self.minority : self.metric.FP += 1
      if row.expected != self.minority and row.predicted != self.minority : self.metric.TN += 1

    m = self.metric
    m.tpr        = m.FP / (m.TP + m.FN + self._eps )
    m.tnr        = m.TN / (m.TN + m.FP + self._eps )
    m.precision  = m.TP / (m.TP + m.FP + self._eps )
    m.fpr        = m.FP / (m.TN + m.FP + self._eps )
    m.fdr        = m.FP / (m.FP + m.TP + self._eps )
    m.fnr        = m.FN / (m.FN + m.TP + self._eps )
    m.accuracy   = (m.TP + m.TN) / (m.TP + m.TN + m.FN + m.FP + self._eps )
    m.f1         = ( 2 * m.TP )  / ( ( 2 * m.TP ) + m.FP + m.FN + self._eps )

  def info( self ) : 

    ss =  "Training :\n"
    ss += "\n".join(["    %-15s : %-20s"%(str(k),str(v)) for k,v in self.train.iteritems()if str(k)[0] != "_" ]) 
    ss += "\n"
    ss += "\nTesting :\n"
    ss += "\n".join(["    %-15s : %-20s"%(str(k),str(v)) for k,v in self.test.iteritems() if str(k)[0] != "_" ]) 
    ss += "\n"
    ss += "\nResults Summary :\n"
    ss += "\n    %5s | %25s | %10s | %10s \n    %5s + %25s + %10s + %10s \n" %( "ID", "Value", "Exp Count", "Prd Count", "-"*5, "-"*25, "-"*10, "-"*10 )
    ss += "\n".join(["    %5d | %25s | %10d | %10d "%( v.id, k, v.count_exp, v.count_prd) for k, v in self.values.iteritems()])
    ss += "\n"
    ss += "\n    Confusion Matrix"
    ss += "\n            *Using Minority Class as Positive: " + str(self.minority )
    ss += "\n"
    ss += "\n          | Exp T | Exp F"
    ss += "\n    ----- + ----- + -----"
    ss += "\n    Prd T | %5d | %5d  " %(self.metric.TP, self.metric.FP) 
    ss += "\n    Prd F | %5d | %5d  " %(self.metric.FN, self.metric.TN) 
    ss += "\n"
    ss += "\n    Metrics"
    ss += "\n".join(["    %10s = %d"%(str(k), int(v)) for k,v in self.metric.iteritems() if str(k) not in ["TP", "TN", "FP", "FN"]])   
    return ss

  def __str__( self ) : 
    ss = ""
    ss += "Testing : === Predictions on test data ===\n"
    ss += "\n"
    ss += "Test# Expct Prdct Reslt\n"
    ss += "\n".join( [ self.sformat.format(x.result, x.expected, x.predicted, x.result) for x in self.result ] ) +"\n"
    return ss
