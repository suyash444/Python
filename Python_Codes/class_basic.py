class A:

    def dog(self):
        x = int(input("Enter the number:"))
        for i in range(2, x):

            if x % i == 0:
                print(f"{x} is a  not prime number")

                break

        else:
            print(f"{x} is  a prime number:")


c1 = A()
c1.dog()
