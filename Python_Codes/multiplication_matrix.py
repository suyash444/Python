## - convert one dimension array to three -dimensional

from numpy import *
arr1 = array([1,3,4,5,6,7,8,9])
arr2 = arr1.reshape(2,4) #-- it tells 2 rows and 4 columns

print(arr2)



## multiplying two array

m1 = array([1,2,3,4,5,6])
m2 = array([7,8,9,1,4,5])
m3 = m1*m2
print(m3)

## multiplying two array in matrix form
## - to multply matrix values should be seperated by semicolon and no comma should be there to form matrix
m3 = matrix('1 2 3 ; 4 5 6 ; 6 7 8')
m4 = matrix('7 8 7; 4 5 4;  5 3 9')

m5 =m3*m4
print(m5)
