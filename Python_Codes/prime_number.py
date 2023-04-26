# write a code that takes input from the user and tell whether the number is a prime or not

a = int(input("Enter the number:"))
for i in range(2,a):
    if a % i ==0:
        print(f"{a} = is not prime number")
        break
else:
    print(f"{a} = is a prime number")