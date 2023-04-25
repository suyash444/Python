pos = -1


def search():
    num = int(input("Enter the number:"))
    i = 0
    list = [0, 1, 2, 4, 55, 41, 6, 7]
    for i in range(len(list)):
        if list[i] == num:
            globals()['pos'] = i

            print("The element found at the position:", pos)
            break
    else:
        print("Not found:")


search()
