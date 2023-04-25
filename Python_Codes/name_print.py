def name():
    a = "suyash singh"
    for i in range(6):
        print(a)


name()


# odd or even

def odd_even():
    num = int(input("Enter the number:"))
    if num % 2 == 0:
        print(f"{num} is a even number")
    else:
        print(f"{num} is a odd number")


odd_even()


# prime numbers

def prime_number():
    num = int(input("Enter the number:"))
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")


prime_number()


# prin the prime numbers till 100

def prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
            break

    return Trueor i in range(2, 101):
    if prime(i):
        print(i)
