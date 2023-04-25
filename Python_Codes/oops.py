# thsi is how we create the class in python
class Computer:

    def abc(self):# when defining method inside the class then self will be taken as object parameter
        x = int(input("Enter the first number:"))
        y = int(input("Enter the second number:"))
        ans = x+y
        print("sum  of two numbers are:", ans)


c1 = Computer() # created the object
c1.abc()