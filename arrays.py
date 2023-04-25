from array import *
arr = array('i',[2,3,4,5])
arr.reverse()
for i in range(4):
    print(arr[i])
## write a code in python to copy the previous values from array and assign to a new array
## python code in array that takes the value from the previous array and print the square of the value
from array import *
value = array('i',[2,3,4,5])
newArray = array(value.typecode,(a*a for a in value))
for e in newArray:
    print(e)
for n in value:
    print(n)
