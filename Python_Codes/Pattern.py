## question write a python program to print this pattern
#  ---
# # # #
# # # # #
# # # # #
# # # # # ------ pattern

for i in range(4): # i reprensent the rows
    for j in range(4):  # j reperesent the columns
        print("#",end=" ")
    print()

# questino--) write a python program to print the pattern


for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()


# python program to print the reverse pattern

for i in range(4):
    for j in range(4-i):
        print("*",end="")
    print()