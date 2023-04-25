# as in python abstract method dont support so that we have to import the module for the abstract method

from abc import ABC, abstractmethod


class A(ABC):
    def work(self):
        pass


class B(A):
    def work(self):
        print("its running:")


class C:
    def process(self):
        print("we do hard work:")


c1 = B()
c1.work()
c2 = C()
c2.process()
