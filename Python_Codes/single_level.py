class A:
    def feature1(self):
        print("Feature 1 working:")

    def feature2(self):
        print("Feature 2 working:")

class B(A):
        def feature3(self):
            print("Feature 3 working:")

        def feature4(self):
            print("Feature 4 working:")

a1 =B()
a1.feature1()
a1.feature2()
a1.feature3()
a1.feature4()