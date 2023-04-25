class Computer:
    def __init__(self, cpu, ram, hardisk):
        self.cpu = cpu
        self.ram = ram
        self.hardisk = hardisk

    def config(self):
        print("configuration of the system is:", self.cpu, self.ram, self.hardisk)


# now call the object and pass the arguments in that two arguments that you have to pass:


c1 = Computer('i7', 16, 552)
c2 = Computer('i9', 32, 556)

c1.config()
c2.config()


class Sample:

    def __init__(self):
        self.name = 'suyash'
        self.age = 27

    def purpose(self):
        self.name = 'Utkarsh'
        self.age = 30

    def a(self):
        self.name = 'anita'
        self.age = 50


c3 = Sample()
c4 = Sample()
c5 = Sample()

c3.__init__()
c4.purpose()
c5.a()

print(c3.name)
print(c3.age)

print(c4.name)
print(c4.age)

print(c5.name)
print(c5.age)
