string = "abracadabra"

# how to change the tuples as they are immutable
l = list(string)
print(l)
l[5] ='K'
print(l)


string = ''.join(l)
print(string)