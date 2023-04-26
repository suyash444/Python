# this way you handle the exception
a = 5
b = 0
try:
    print(a / b)
except Exception:
    print("The number cannot be divived by zero")

print("bye")

# how to print the error in the exception what error is getting

a = 3
b = 0

try:
    print(a/b)
except Exception as e:
    print("The error that we are getting",e) # division by zero this is the error that we are getting

print("bye")


# finally  block::

a = 450
b = 0

try:
    print(a/b)
    print("executed:")

except Exception as e:
    print("result block executed", e)

finally:
    print("all above statements executed successfully:")