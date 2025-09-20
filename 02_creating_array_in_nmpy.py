import numpy as np

# creating array from python list
# np.array([e1,e2,e3,....])


arr = np.array([1,2,3,4,5])
print(arr)



#  creating array with defualt value for future values

#  np.zeros(shape) shape=3 for 1D , (2,3) for 2D
zeros_arr = np.zeros(3)
zeros_arr1 = np.zeros((3,2))
print(zeros_arr1)


#  np.ones(shape) shape=3 for 1D , (2,3) for 2D
ones_arr = np.ones(3)
ones_arr1 = np.ones((3,2))
print(ones_arr1)


#  np.full((shape),constant) shape=3 for 1D , (2,3) for 2D
full_arr = np.full(3 , 2)
full_arr1 = np.full((3,2) ,4)
print(full_arr1)


# creating squecnce of numbers in numpy
#  np.arange(start , stop , step)
arange_arr = np.arange(10)
arange_arr1 = np.arange(1,10,2)
print(arange_arr1)


#  creating identity matrix
#  np.eye(size) size=4 
identity_matrix = np.eye(4)
print(identity_matrix)