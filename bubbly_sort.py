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

def array_sort(data, array_size):
   for k in range(array_size ):
      if not float_largest_to_top(data, array_size - k):
         return

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

# client --------------------------------------------
# my_array = ["mark", "andrea", "zebra", "aardvark"]


my_array = [10.2, 56.9, -33, 12, 0, 2, 4.8, 199.9, 73, -91.2]
array_size = len(my_array)

print_array(my_array, array_size, "Our array before the sort")
array_sort(my_array, array_size)
print_array(my_array, array_size, "\n\nAnd now after the sort")

""" --------------------------- RUN ---------------------------
Our array before the sort

10.2, 56.9, -33, 12, 0
2, 4.8, 199.9, 73, -91.2

And now after the sort

-91.2, -33, 0, 2, 4.8
10.2, 12, 56.9, 73, 199.9
------------------------------------------------------------ """