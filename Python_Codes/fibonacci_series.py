x = int(input("Enter the number:"))


def series():
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2, x):
        c = a+b
        a = b
        b = c
        print(c)

series()

def fib(num):
    if(num<0):
        print("Invalid number")
    else:
        a=0
        b=1

        print(a)
        print(b)

        for i in range(num+1):
            c=a+b
            a=b
            b=c
            if(c<=num):
                print(c)
            else:
                break
num=int(input("Enter the number till you want to see in fibonacci series : "))
fib(num)

# fibonacci series

a1 = int(input("Enter the number:"))
def fibonacci(a1):
    x = 0
    y = 1
    print(x)
    print(y)
    for i in range(2,a1):
        z = x+y
        x = y
        y = z
        print(z)


fibonacci(a1)