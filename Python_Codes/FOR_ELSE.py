# question -- give a list of numbers and you have to print the numbers that are divisible by 5 only

a = [12,10,25,5,11,19]
for num in a:
    if num %5 == 0:
        print(num)



## for else program example

ab=[10,12,5,23,22,3,33]
for i in ab:
    if i%5 ==0:
        print(i)
        break
else :
    print("not found")


# question -- check whether the given number is a prime or not

#  num = int(input("enter the number:"))
# for i in range(num):
#     if num % i == 0:
#         print("number is not a prime:")
#         break
# else:
#     print(" prime") */

def is_prime(num):
    # 0 and 1 are not prime numbers
    if num < 2:
        return False
    # 2 is a prime number
    elif num == 2:
        return True
    # check for other even numbers
    elif num % 2 == 0:
        return False
    else:
        # check for odd numbers
        for i in range(3, int(num**0.5)+1, 2):
            if num % i == 0:
                return False
        return True

# take input from user
num = int(input("Enter a number: "))

# check if number is prime or not
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# write a code to find the prime number from the user input

n1 =int(input("Enter the number:"))
for i in range(2, n1):
    if n1% i ==0:
        print("number is not prime")
        break
else:
    print("number is prime")