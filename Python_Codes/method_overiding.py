# method defining the overiding prograam

class A:
    def show(self):
        print("It is a A method")


class B(A):  # this is method verrinding same methodname and same arguments
    def show(self):
        print("It is a B method")


c1 = B()
c1.show()