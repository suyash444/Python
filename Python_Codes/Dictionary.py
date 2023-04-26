# Dictionaries also uses curly brackets and in dictinaries we use keys and values
# example a= {'a' :1, 'suyash':'singh}
# so here 'a' -- is key and 1 is values
# so here 'suyash' is a key and 'singh' is a values

#example dictionaries

data ={'name':'suyash', 'abhay':'loves','a': 23}
print(data)

print(data['name'])
# here name is a key and answer 'suyash' is a value returing

print(data.get('a'))
# here 'a' is a key and 23 answer is a vaalue
print(data.get(3, 'new'))
# new ---- answer
# it will assign 3 as a new as 3 was not defined so it will assign 3 as a value

## zip the dictionaries

keys =['a','b','c']
values =['python','suyash','mohan']
data = dict(zip(keys,values))
print(data)

# it will return in dictionaries as a key and values


# add key and values in dictinaries

data['utkarsh']= 'CS'
print(data)

# {'a': 'python', 'b': 'suyash', 'c': 'mohan', 'utkarsh': 'CS'} it added as we can see the answer

# now remove the dictionaries key and value

del data['a']
print(data)

# {'b': 'suyash', 'c': 'mohan', 'utkarsh': 'CS'} -- now deleted the key 'a'


## dictionaries in list and didctionaries in dictionaries

data_new = {'name':'suyash', 'abhay':'loves','a': ['python','suyash','mohan'],'Java':{'a':1,'b':2}}
print(data_new)
#  answer -- {'name': 'suyash', 'abhay': 'loves', 'a': ['python', 'suyash', 'mohan'], 'Java': {'a': 1, 'b': 2}}
#  where -- 'a': ['python', 'suyash', 'mohan'] 'a' is a key and all the values in list is a values
# 'Java': {'a': 1, 'b': 2}} : similarily java is a key and {} and inside its a values
print(data_new['a'])
print(data_new['Java']['b'])
# 2 -- answer as java is key and 'b' is a subkey nd 'b' value is 2
print(data_new['a'][0])
# python --- answer python because index 0 is a python
