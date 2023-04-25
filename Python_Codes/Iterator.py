# so this iter keyword is used to iterate the values in python

nums = [3, 4, 5, 6, 8, 7]
a = iter(nums)
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
#
# # second way to print the next value
#
# print(next(a))
# with the help of for loop we can print all the values
for i in nums:
    print(i)