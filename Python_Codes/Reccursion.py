def func(x):
    if x <= 1:
        return 1
    else:
        return x * func(x-1)


print(func(5))
