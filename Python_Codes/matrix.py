from numpy import *
arr1 = array([[1,3,4,5,6],
             [2,4,65,66,1]])
print(arr1.dtype)
## -dtype will tell whether the given array is int or float

## number of dimensions in array
print(arr1.ndim) #-- as it is two dimensional array so the answer will also be 2

## how to convert two dimensional array into one dimensional array
## -- output [ 1  3  4  5  6  2  4 65 66  1]
arr2= arr1.flatten()
print(arr2)