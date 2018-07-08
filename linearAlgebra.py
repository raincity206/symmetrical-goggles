import numpy as np
a_vector = np.array([1,2,3,4])


## Arange
# Arange includes the start parameter 
# and excludes the stop value
# you can also use the step parameter


arange_vector1 = np.arange(25)
arange_vector2 = np.arange(10,25)
arange_vector1.size

#You can often accomplish the same tasks using either
#Python or NumPy

some_tuple = (12, -4.99, 5.00+7j)

print(some_tuple)
print(some_tuple*5)
print(np.array(some_tuple)*5)


### linspace(), zeros(), ones() and numpy data types
# linspace() creates an array whose elements are evenly spaced