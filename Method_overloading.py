class A:
    def sum(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        s = 0
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
            
        else:
            s = a

        return s


c1 = A()

print(c1.sum(10, 20))
