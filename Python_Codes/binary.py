pos = -1


def search(list, num):
    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (l + u) // 2
        if list[mid] == num:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < num:
                l = mid + 1
            else:
                u = mid - 1
    return False


list = [1, 2, 3, 4, 5, 6, 7, 8]

num = int(input("Enter the number:"))
if search(list, num):
    print("found the number", pos)
else:
    print("not found")
