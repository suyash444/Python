# question -- swapping of two numbers in python using rotation method

a= 5
b =3

a,b = b,a
print(a)
print(b)


# question --- swapping of two numbers without using the third variable
# -- input the number by yourself

a= int(input("Enter the first number:"))
b= int(input("Enter the second number:"))
a = a+b
b = a-b
a= a-b

print(" The value of a after swapping is:",a)
print(" The value of b after swapping is:",b)

# question -- swapping of two numbers using third variable temporary variable in python

x= int(input("Enter the first number:"))
y = int(input("Enter the second number:"))



##question   ##--- swapping using the third temporary variable

temp = x
x= y
y = temp

print(" The value of x after swapping is:",x)
print(" The value of y after swapping is:",y)