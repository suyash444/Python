def statement():
    for i in range(5):
        a = int(input("Enter the score:"))
        b = int(input("Enter the age:"))

        if b <= a:
            print(a)

        elif a == b:
            print(b)

        else:

            print(a, b)


statement()