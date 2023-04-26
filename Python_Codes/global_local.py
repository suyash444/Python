a = 10 #-- this is called global variable
def function():
    a= 20 #-- this is called local variable
    print("This is local variable:",a)
function()
print("This is global variable",a)


# now how to convert local variable to global variable see
a =40
def abc():
    global a #-- we defined the keyword as global so it will be considered as a glolbal value now everywhere
    a=60
    print("inside value",a)
abc()
print("now the global variable value be",a) #-- it changed to 60 because we defined the keyword as global now