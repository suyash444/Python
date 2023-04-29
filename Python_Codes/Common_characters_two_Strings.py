def func():
    a = input("Enter the first String:")
    b = input("Enter the second String:")

    x1 = set(a)
    x2 = set(b)

    result = x1 & x2

    print("the common characters in both the string are:", result)


func()
