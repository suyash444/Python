pos = -1


def search():
    a = int(input("Enter the number:"))
    i = 0
    list = [2, 3, 4, 44, 1, 21, 23]
    for i in range(len(list)):
        globals()['pos'] = i
        if list[i] == a:
            print("The number is found:", pos)
            break
    else:
        print("The number is not found: ")


search()