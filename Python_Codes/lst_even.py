lst = [12,2,3,4,5,66,87,99,90]
def count(lst):
    even = 0
    odd = 0
    for i in lst:

        if i % 2 ==0:
            even+=1
        else:
            odd+=1
    return  even,odd
even,odd = count(lst)
print(even)
print(odd)


#-- second questiom
a=[]
for j in range(5):
    x =input("Enter the user name:")
    a.append(x)
#a=['suyash','mohan','ram','utkarsh','anita','shubham','ankit','jeevan','abhay','mayank','ab']
def count(a):
    greater = 0
    lesser = 0
    for i in a :
       if len(i)>=5:
           greater+=1
       else:
           lesser+=1
    return greater,lesser
greater,lesser = count(a)
print("The names with more than 5 letters are:",greater)
print("The names with less than 5 letters are:",lesser)
print("greater = {} and lesser ={}".format(greater,lesser))