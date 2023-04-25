class A:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def show(self):
        print(self.name, self.roll_no)

    class B:
        def __init__(self, brand, CPU, ram):
            self.brand = brand
            self.cpu = CPU
            self.ram = ram

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = A('SUYASH', 4)
S2 = A('Shubham', 8)
print(s1.name, s1.roll_no)
print(S2.name, S2.roll_no)


c1 = A.B('Nokia','I5',32)
c2 = A.B('Samsung','I7',64)
print(c1.brand,c1.cpu,c1.ram)
print(c2.brand,c2.cpu,c2.ram)


class Fib():

    def pou(self):
        n =int(input("enter the number:"))
        x= 0
        y =1
        print(x)
        print(y)

        for i in range(2, n):
            #condition for fibonacci series
            z = x+y
            x =y
            y= z

            print(z)

c1 = Fib()
c1.pou()


