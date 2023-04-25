from array import *

arr = array('i', []) # create an empty array that values can be inserted in it
a = int(input("Enter the length of the array:"))
for i in range(a):
    b = int(input("enter the value:"))
    arr.append(b)
print(arr)

x = int(input("Enter the number you want to print its index value:"))
# k = 0
# for e in arr:
#     if e ==x:
#         print(k)
#         break
#     k+=1

print(arr.index(x))


