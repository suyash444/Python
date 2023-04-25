def add():
    a = int(input("Enter the number:"))
    b = int(input("Enter the second number:"))
    c= a+b
    print(f"The sum of two numbers is ={c}")
add() #--  # -- always call the function otherwise it will not give the output

# second method to pass the arguments in the function

def add1(x,y):
    ans = x+y
    print(f"The sume of two numbers is ={ans}")
add1(3,10)  # -- always call the function otherwise it will not give the output

# third method to return the function
def add_sub(a1,b1):
    num = a1+b1
    num1= a1-b1
    return num,num1
result1= add_sub(5,4)
print(result1)