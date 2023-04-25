
ab ={'Ram': 'A','Suyash':'Iphone','Abhay':'apple'}
print(ab.keys())

# --dict_keys(['Ram', 'Suyash', 'Abhay'])

print(ab.values())
#-- dict_values(['A', 'Iphone', 'apple'])

# -- its telling the type of ab which is dictionaries
print(type(ab))


#-- range

ad = range(10)
print(ad)
# -- range(0, 10) answer

a =list(range(10))
print(a)
# -- [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] -- answer

b = list(range(1,20,2))
print(b)
## -- [1, 3, 5, 7, 9, 11, 13, 15, 17, 19] -- answer as starting index 1 and end with 20 leaving one number


# --- boolean operators
a,b = 12 ,13
print(a>b)

print(a<b)
## -- relational operators -- and , or , not
print(a==b)

print(a>=b)
print(a<=b)

print(a!=b)


x ,y =2,10
print(x<12 and y >1)
