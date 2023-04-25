# example of multiple inheritance

class A:
    def feature1(self):
        print("hello")
class B:
    def feature2(self):
        print("Hello 2")


class C(A,B): # MULTIPLE INHERITANCE
    def feature3(self):
        print("Hello 3")


c1 =C()
c1.feature1()
c1.feature2()
c1.feature3()