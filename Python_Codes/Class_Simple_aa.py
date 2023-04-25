class A:

    def __init__(self):
        self.a = 0
        self.b = 0

    def add(self):
        self.a = int(input("Enter the first number:"))
        self.b = int(input("Enter the second number:"))


class B(A):
    def result(self):
        ans = self.a + self.b
        print("Addition of two numbers is :", ans)


c2 = B()

c2.add()
c2.result()

for i in range(5):
    a ="suyash"
    print(a)