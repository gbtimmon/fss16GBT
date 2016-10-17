from Table import Reader, Table 

def KNN( train_file, test_file, k ) : 
  train = Reader( train_file ).table()
  test  = Reader( test_file  ).table()

 
