"""
    senario : 10% of discount on each product of different price 
    let's suppose [100,200,300]
"""
""" problem with python"""
prices_list = [100  , 200 ,300,400,500]
discount = 10  #10% discount

discounted_prices_list = []

for price in prices_list:
    discounted_price = price - (price*discount/100)
    discounted_prices_list.append(int(discounted_price))

print("prices_list : ", prices_list)
print("discount_prices_list : ",discounted_prices_list)


""" solution with numpy"""
import numpy as np
prices = np.array(prices_list)
print(prices - (prices * discount / 100))


""" broadcasing in numpy 
    broadcast(scallar) scallar -> element
"""
""" for single array """
arr = np.array([100 , 200, 300, 400])
print(arr + 10)
print(arr * 2)



""" for double arraya """
# arr1 = np.array([[1,2,3] , [4,5,6]]) #shape(2,3)
# arr2 = np.array([1,2]) #shape(2,) this will throw error
arr1 = np.array([[1,2,3] , [4,5,6]]) #shape(2,3)
arr2 = np.array([1,2,3]) #shape(2,)

result = arr1 + arr2
print(result)



"""
    let's try vectorization in python
"""
list1 = [[1,2,3],[4,5,6]]
list2 = [1,1,1]


# result = []   # to store the new rows
# for row in arr1:              # loop over each row in arr1
#     new_row = []              # build a new row
#     for i in range(len(arr2)):
#         new_row.append(row[i] + arr2[i])   # element-wise addition
#     result.append(new_row)    # add the row to the result

result = [[a+b for a,b in zip(row , list2)] for row in list1]
print(result)
