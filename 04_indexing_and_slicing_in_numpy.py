"""
    indexing and slicing in numpy
    acess element of array in different ways

    -> indexing
    -> slicing
    -> fancy indexing
    -> boolean masking

"""

""" indexing in numpy array
    array[index]  #1d array
    array[row , column]  #2d array
"""


import numpy as np

idx_arr = np.array([1,2,3,4,5,6,7,8,9,10])
print([0])  #first element
print([2])  #3 0 base
print([-1]) #last element 


""" slicing in numpy array (selecing more than one element in a squence)
    array[start:stop:step]  
"""

slice_arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(slice_arr[1:5])   #index 1 to 4
print(slice_arr[:4])   #index 0 to  3
print(slice_arr[::2])   #index 0 to last  every second element
print(slice_arr[::-1])   #reverse the array


""" fancy indexing in numpy array (selecing multipule at element once)
    array[[index, index, index , ...]]  
"""

fanc_arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(fanc_arr[[0,2,5]])    #output:[1 3 6]

""" Boolean masking in numpy array ( conditions (True or False))
    array[condition]
"""

blm_arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(blm_arr[blm_arr > 5])    #output:[ 6  7  8  9 10]




