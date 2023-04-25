# this is the example of multilevel inheritance

class A:
    def feature1(self):
        print("1")

class B(A):
    def feature2(self):
        print("2")

class C(B):
    def feature3(self):
        print("3")

a1 = C()
a1.feature1()
a1.feature2()
a1.feature3()
        