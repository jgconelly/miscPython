"""
Example of bubble sort. 
"""

def float_largest_to_top(data, array_size):
   
   changed = False
   
   # notice we stop at array_size-2 because of expr. k+1 in loop
   for k in range(array_size - 1):
      if (data[k] > data[k + 1]):
         data[k], data[k+1] = data[k + 1], data[k]
         changed = True;
   return changed

def print_array(data, array_size,
               optional_title = "--- The Array -----------:\n"):
   ITEMS_PER_LINE = 5
   print( optional_title )

   # new line every ITEMS_PER_LINE items, commas between
   for k in range(array_size):
      if (k % ITEMS_PER_LINE == 0):
         print()           
      else:
         print( ", ", end = '' )     
      print ( data[k], end = '' )