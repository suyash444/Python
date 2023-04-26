names = ("Suyash", "Harsh", "Swapnil", "Mohan", "Manish")
companies = ("Dell", "Apple", "Google", "Amazon", "Kyndryl")

zipped = list(zip(names, companies))
print(zipped)

# using for loop also we can do

# defining for loop
for (a, b) in zipped:
    print(a, b)
