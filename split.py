# def split_and_join(line):
#
#
#     if __name__ == '__main__':
#         line = input("Enter the String:")
#         result = split_and_join(line)
#         print(result)
#
#
# split_and_join()



a = "My name is Suyash Singh"
a = a.split(" ")
print(a)
b = "-".join(a)
print(b)

a = "this is a string"
a = a.split(" ") # a is converted to a list of strings.
print (a)
a = "-".join(a)
print (a)

# ['My', 'name', 'is', 'Suyash', 'Singh']
# My-name-is-Suyash-Singh
# ['this', 'is', 'a', 'string']
# this-is-a-string


def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line

if __name__ == '__main__':
    line = input("Enter the String:")
    result = split_and_join(line)
    print(result)
