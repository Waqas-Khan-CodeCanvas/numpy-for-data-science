# python vs numpy

# average in python 
temp_list = [23.5,34.5 , 45.5 , 65.5, 25.5 ]
total = 0 
for temp  in temp_list:
    total += temp

average = total / len(temp_list)
print(average)


# average in numpy 
import numpy as np

np_temp_list =np.mean( np.array(temp_list))
# np_average  = np.mean(np_temp_list)
print(np_temp_list)


# -> speed calculations
# -> less memory and efficient management of memory
# -> easy math operations

# -> Data Sceince 
# -> ML (Ai)
# -> stock market finance
# -> Medical Research 
# -> Image processing


# python  list             vs numpy array
# speed slow                 faster
# memory more               less and efficient 
# calculation need loops    without loops
# best for small dataset    for large data set

python_list= [1,2,3,4,5,6]
print(python_list)

numpy_list  = np.array([1,2,3,4,5,6,7])
print(numpy_list)

#  1D array
arr_1d = np.array([1,2,3,4,5,6,6])

#  2D array
arr_2d = np.array([[1,2,6,6],
                    [1,2,6,6],
                    [1,2,6,6]])
print(arr_2d)


# multi-dinesional array
matrix = np.array([[1,2,3,4],
                   [5,6,7,8,9],
                   [[1,2,3],[4,5,6]]])
print(matrix)

