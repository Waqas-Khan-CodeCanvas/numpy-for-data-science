"""
    Reshaping and manipulating array in numpy (change dimensions style without modifying data)
    reshape(rows,columns) specify new shape (if dimensions match)
    -> note: reshape dose not create copy it create view of original array
"""

import numpy as np

sh_arr=np.array([1,2,3,4,5,6,7,8,9,10])
reshaped_arr = sh_arr.reshape(2,5)
print(reshaped_arr)    

""" output:
    [[ 1  2  3  4  5]
    [ 6  7  8  9 10]]
"""



"""
    flattening array in numpy (array.ravel() -> view , array.flatten() -> copy)
    convert multi-dimenssional array to 1D
"""

arr_2d = np.array([[ 1,  2 , 3 , 4,  5],[ 6  ,7 , 8 , 9, 10]])
print(arr_2d.ravel())
print(arr_2d.flatten())



"""
    let's summerize what we have learned (topics)

    -> indexing
    -> slicing
    -> fancy indexing
    -> boolean masking
    -> array shape
    -> ravel , flattten

"""


"""
    manipulating array in numpy (add, remove , stack , split , merge) 

    -> insert()
    -> append()
    -> delete()
    -> stack()
    -> hstack()
    -> vstack()
    -> split()
    -> hsplit()
    -> vsplit()
    -> concatenate()
"""



"""
    np.insert(array , index , value , axis=None)
    axis=0 for row-wise insertion
    axis=1 for column-wise insertion

"""


append_arr_1d = np.array([10,20,30,40,50,60])
print(append_arr_1d) #output:[10 20 30 40 50 60]
new_arr = np.insert(append_arr_1d,2,90)
print(new_arr)  #output:[10 20 90 30 40 50 60]


append_arr_2d = np.array([[1,2,3,4],[5,6,7,8]])
new_arr = np.insert(append_arr_2d,1,[80,90],axis=None) #insert a new row
print(append_arr_2d) #output:[[1,2,3,4],[5,6,7,8]]
print(new_arr)  #output:[ 1 80 90  2  3  4  5  6  7  8]




"""
    np.append(array , [elements])
    add element at the last
"""
print("array append methods")

append_arr_1d = np.array([10,20,30,40,50,60])
print(append_arr_1d) #output:[10 20 30 40 50 60]
new_arr_1 = np.append(append_arr_1d,200)
print(new_arr_1)  #output:[10 20 90 30 40 50 60,200]


append_arr_2d = np.array([[1,2,3,4],[5,6,7,8]])
new_arr_2 = np.append(append_arr_2d,[80,90]) #insert a new row at last
print(append_arr_2d) #output:[[1,2,3,4],[5,6,7,8]]
print(new_arr_2)  #output:[ 1  2  3  4  5  6  7  8 80 90]




"""
    np.delete(array , index , axis=None)
    flatten array
"""
print("array delete methods")

del_arr1d = np.array([10,20,30,40,50,60])
print(del_arr1d) #output:[10 20 30 40 50 60]
new_del_arr = np.delete(del_arr1d,0) #0 -> index
print(new_del_arr)  #output:[20 90 30 40 50 60]



del_arr2d = np.array([[1,2,3],[4,5,6]])
print(del_arr2d) #output:[[1,2,3],[4,5,6]]
new_del_arr2d = np.delete(del_arr2d,0 , axis=0) #0 -> index
print(new_del_arr2d)  #output:[[4 5 6]]



"""
    stacking array in numpy
    -> stack( )
    -> vstack( )    row wise
    -> hstack( )    column wise
"""
print("array stacking methods")

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(np.vstack((arr1,arr2)))   #vertically stack output:[[1 2 3][4 5 6]]
print(np.hstack((arr1,arr2)))   #horizontally stack output:[1 2 3 4 5 6]



"""
    spliting  array in numpy
    -> split( ) equal size
    -> vsplit( )    
    -> hsplit( )   
"""
print("array splitin methods")

arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(np.split(arr1 , 2)) # must be divide into equal parts other wise this will throw ValueError:

