# print the code to get how many candies you get if the user input the command

a = int(input("How many candies you want:"))
i = 1
# for i in a:
while i <= a:
    print("candies")
    i += 1

for i in range(0, 100):
    if i % 3 != 0 :
     if i% 5 != 0:
        print(i)


## break statement

ai = 5
x = int(input("How many candies you want:"))
i =1
while i <=x:
    if i>ai:
        break
    print("Cndies")
    i+=1

print('running out')


# pass in python

for i in range(0,100):
    if i%2 ==0:
        pass
    else:
        print(i)


# pass is basically used to pass the argument if we are not writing any statement after if else or elif just pass the statemnet in python


