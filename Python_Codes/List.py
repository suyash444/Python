new = [1, 2, 3 ,4 ,5 ,6] # anything in [] is called the list --it is called the list
print(new)


names =['suyash','mohan','aman', 'utkarsh']  # in list strings can also be taken
print(names)


mil =[new,names]
print(mil)

names.append('manish') # list is mutable as we can append and do many functions in list we can change value aslo
print(names)

print(new)
new.pop(0) # to remove one element in list using index
print(new)

new.insert(0,11) # to insert new element in list
print(new)

# delete multiple values

del new[0:2] # it will delete from index number zero to index number 1

print(new)

# want multiple values

new.extend([1,2,33,34])
print(new)


#minimum value

print(min(new))

#maximum value

print(max(new))

# sort the list in ascending order
new.sort()
print(new)