def odd_even():
    n = int(input("Enter the number:"))
    if n % 2 != 0:
        print("Weird")

    elif n % 2 == 0 and n in range(2, 6):
        print("Not Weird")

    elif n % 2 == 0 and n in range(6, 21):
        print("Weird")

    elif n % 2 == 0 and n > 20:
        print("Not weird")

    else:
        print("Not Applicable")


odd_even()


n = 3

if n % 2 != 0:
    print("Weird")
elif n in [2, 4]:
    print("Not Weird")
elif n in range(6, 21):
    print("Weird")
elif n in [3]:
    print("Not Weird")
else:
    print("Not Weird")