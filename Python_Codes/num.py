import numpy as np
a = np.array([2,3,4,5])
print(a[0:2])


import numpy as np
x= np.array([[1,4,6,3], [2,4,5,9],[3,4,6,5]])
print(x.dtype)


# python program to print the prime numbers that take input from the user

num = int(input("Enter the number:"))
for i in range(2,num):
    if num % i ==0:
        print(f"{num}:- is not a prime number")
        break
else:
    print(f"{num}:- is a prime number")
