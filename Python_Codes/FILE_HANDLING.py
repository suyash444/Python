# so 'r' is a read command to read the data
f = open('MY_TEXT', 'r')
print(f)  # to read the file name
# output
# <_io.TextIOWrapper name='MY_TEXT' mode='r' encoding='cp1252'>


print(f.read())  # it will read all the data in the file
# output
# HELLO SUYASH
# I AM A VERY GOOD BOY
# SUYASH SINGH IS GOOD
# BYE SEE YOU TOMORROW

# to read only first line tehn we use .readline()
f = open('MY_TEXT', 'r')
print(f.readline(), end='')
print(f.readline())

# it will create file abc_txt so 'w' is a write command

f1 = open('abc_txt','w')
f1.write("suyash is a good boy")
f1.write("hello")

# append

f2 = open('abc_txt','a')
f2.write("i am suyash")