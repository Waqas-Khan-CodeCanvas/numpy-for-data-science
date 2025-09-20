""" 
        array properties and methods (shape , size , type)
        number of dimentions 

        for example you are a warehouse manager
        product name , quantity , price shape
"""

import numpy as np 

arr_2d=np.array([[1,2,3],
                [4,5,6]])

print(arr_2d.shape)  # output : (2,3) 2 -> row , 3 -> column

# size total number item in array or list
arr_size = np.array([[2,3,4],[2,3,4]])
print(arr_size.size)

# array dimentions no of dimentions 1D , 2D , 3D
ndim_of_arr = np.array([[2,3,4],[2,3,4]])
print(ndim_of_arr.ndim)

# datatype of array (array.dtype) int , float , str
type_arr = np.array([2,3,4,5,5,6])
print(type_arr.dtype)

# type casting in numpy array
float_arr= np.array([2.3,3.3,4.3,5.3,5.3,6.3])
int_arr = float_arr.astype(int)

print(float_arr)
print(int_arr)
print(int_arr.dtype)


#  operators in numpy (+,-, * , ** , %, /)
op_arr = np.array([1,2,3,4,5,6])

print(op_arr + 2)
print(op_arr * 2)
print(op_arr ** 2)


"""     aggregation functons in numpy
        function                what is dose

        -> np.sum(array)        add all array elements
        -> np.mean(array)       calculate average
        -> np.min(array)        min in array
        -> np.max(array)        max in array
        -> np.std(array)        standard deviation
        -> np.var(array)        variance
        
"""

agg_arr = np.array([10,20,30,40,50])

print("sum of array is : ",np.sum(agg_arr))
print("mean of array is : ",np.mean(agg_arr))
print("max of array is : ",np.max(agg_arr))
print("min of array is : ",np.min(agg_arr))
print("std of array is : ",np.std(agg_arr))
print("var of array is : ",np.var(agg_arr))


