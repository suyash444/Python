pos = -1


def search(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i + 1
    return False


list = [1, 32, 4, 5, 98, 12, 222, 111, 0000, 1222, 23, -1]
n = -1
if search(list, n):
    print("the element found at the position at:", pos)

else:
    print("the element not found:")

# linear search using for loop

pos = -1

# linear seach using input enter a number from user
pos = -1


def linear_Search():
    n = int(input("Enter the number:"))
    i = 0
    list = [1, 2, 3, 4, 5, 6, 7]
    for i in range(len(list)):
        if list[i] == n:
            globals()['pos'] = i
            print("found psoition:", pos)
            break
    else:
        print("Not found")
c1 = linear_Search()