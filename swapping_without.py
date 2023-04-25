def swap():
    x = int(input("Enter the  first number:"))
    y = int(input("Enter the second number:"))

# before swapping values of x and y

    print("Value of x before swapping is ", x)
    print("Value of y before swapping is ", y)

# condition of swapping two numbers without using third variable

    x = x+y
    y = x-y
    x = x-y

# value after swapping

    print("Value of x after swapping is ",x)
    print("Value of y after swapping is ",y)


swap()


# shortcut method

def swap1():
    x= 4
    y =5
    print(x)
    print(y)
    x,y = y,x

    print(x)
    print(y)

swap1()

# swapping of two numbers using temporsary variable


def swap2():
    x = 1
    y = 2

    print(x)
    print(y)

    temp = x
    x = y
    y = temp

    print(x)
    print(y)


swap2()