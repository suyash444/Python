#-- how to copy an array from one array to another array

from numpy import *
arr1 = array([2,3,4,5,6])
arr2 = arr1

print(arr1)
print(arr2)
####--- to check the address of the array we will print the id of the array so the address wil also be the same
print(id(arr1))
print(id(arr2))


#-- two type of copy are there which are used in array: 1: shallow copy and 2: is deep copy

#1:) shallow copy
from numpy import *
arr1 = array([2,3,4,5,6])
arr2 = arr1
arr1[1]= 11
print(arr1)
print(arr2)

#-- answer [ 2 11  4  5  6]
#          [ 2 11  4  5  6]  -- this is called shallow copy as copying the same value of array1

#2: deep copy

from numpy import *
arr1 = array([2,3,4,5,6])
arr2 = arr1.copy()
arr1[1]= 11
print(arr1)
print(arr2)
##-- result [ 2 11  4  5  6]
#--          [2 3 4 5 6]  --- this is called deep copy we used copy function