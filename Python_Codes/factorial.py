# --- factorial of a number taken by the user 

x = int(input("Enter the number you want to take factorial:"))


def fact():
    f = 1
    for i in range(1, x+1):
        f = f*i
    return f


result = fact()
print(result)
