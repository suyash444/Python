from threading import *
from time import sleep


class A(Thread):  # to create thread
    def run(self):
        for i in range(5):
            print("Suyash")
            sleep(1)


class B(Thread):
    def run(self):
        for i in range(5):
            print("Singh")
            sleep(1)


t1 = A()
t2 = B()

t1.start()
sleep(0.2)  # this will now print it simultaneously
# to print it simultaneously suyash singh suyash singh we have to use start() that is called threading
t2.start()
t1.join()
t2.join()# to us join to print the statement in between
print("Bye")
