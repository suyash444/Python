#### -- this is called modules in python as if we want to perform the action in other
##-- module or file we will write the code in the 2 modules to fetch the function



# see if we are calling the add() function from the demo module then it should print add function print result
# but its printing all the results so we will use now special variable called name


def a():

    print("result is ", __name__)


def b():
    print("result 2")


def main():
    a()
    b()

if __name__ == "__main__":
    main()

