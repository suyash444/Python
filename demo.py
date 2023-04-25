## -- this is called modules in python as if we want to perform the action in other
##-- module or file we will write the code in the 2 modules to fetch the function

from calc import *
def add ():
    a()
    print("add")
# -- the output that is coming from the code we can see that:
# result is  calc
# add
# sub
# multi
# div

def sub ():

    print("sub")

def multi():

    print("multi")

def div():

    print("div")

def main():
    add()
    sub()
    multi()
    div()

main()