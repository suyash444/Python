lst = []
for i in range(5):
    x = int(input("Enter the numbers:"))
    lst.append(x)


def count(lst):
    even = 0
    odd = 0
    for j in lst:
        if j % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd
even ,odd = count(lst)
print("even numbers ={} and odd numbers ={}".format(even,odd))
