# simple method of printing the square root or with the help of generators also we can do
def TopTen():
    n = 1
    while n <= 100:
        sq = n * n
        yield sq  # Yield expressions and statements are only
        # used when defining a generator function, and are only used in the body of the generator function.
        # Using yield in a function definition is sufficient to cause that definition to create a generator function instead of a normal function.
        n += 1


values = TopTen()
for i in values:
    print(i)


# simple methodf to print th esquare root of ten numbers in python using function

def square():
    n = 1

    while n <= 10:
        sqrt = n * n
        n += 1
        print(sqrt)


square()

# square of ten numbers using for loop
def aa():
    for i in range(1, 11):
        sqrts = i * i
        i += 1
        print(sqrts)


aa()
