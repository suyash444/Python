def func():
    a = input("Enter the first String:")
    b = input("Enter the second String:")

    x1 = set(a)
    x2 = set(b)

    result = x1 & x2

    print("the common characters in both the string are:", result)


func()

# using for loop find the common characters

a1 = input("Enter the first string:")
a2 = input("Enter the second string:")

common_char = ""

for char1 in a1:
    for char2 in a2:
        if char1 == char2:
            common_char += char1

print("common_characters:", common_char)


