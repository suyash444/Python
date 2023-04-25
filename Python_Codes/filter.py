#-- filter out the even numbers from the list given

def is_even(n):
    return n%2 == 0
nums =[2,3,4,5,6,8,9,10]
evens = list(filter(is_even,nums))
print(evens)

## how to use the inbuilt function filter in the python

lst = [2, 4, 6, 12, 24, 5, 6]
even = list(filter(lambda n: n % 2 == 0, lst))
print(even)


## now double the even numbers using the filter function and map ffunction

list1 = [2, 4, 6, 12, 24, 5, 6]
even_number = list(filter(lambda n :n % 2 ==0, list1))
print(even_number)
doubles = list(map(lambda n: n*2 ,even_number))
print(doubles)


def divison(x,y):
    print(x/y)
divison(4,2)
