import sys
def print_results( table, arr, stream=sys.stdout ):
  item_id = 1
  vm = {}

  stream.write("=== Predictions on test data ===\n\n")
  stream.write(" inst#     actual  predicted error prediction\n")
  for idx, i in enumerate(arr) :
    p, e = i

    p = tuple(table.getDependentValues( p ))
    e = tuple(table.getDependentValues( e ))

    if p not in vm :
      vm[p] = item_id
      item_id += 1

    if e not in vm :
      vm[e] = item_id
      item_id += 1

    stream.write( "%d %d %d %s\n"%(idx, vm[p], vm[e], "1" if p == e else "0" ) )
    
    
