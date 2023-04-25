class Hello:
    student ='Suyash'

    def __init__(self, m1 ,m2 ,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return(self.m1 + self.m2 + self.m3)/3

    @classmethod
    def abc(cls):
        return cls.student


c1 = Hello(20, 30, 40)
c2 = Hello(40, 50, 90)

print(c1.average())
print(c2.average())
print(Hello.abc())
print(c1.abc())
