#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first_name, last_name):
    if len(first_name) and len(last_name) <= 10:
        print("Hello" + " " + first_name + " " + last_name + "! You just delved into python.")
        return True
    else:
        return False


if __name__ == '__main__':
    first_name = input("Enter fist name:")
    last_name = input("Enter the second name:")
    print_full_name(first_name, last_name)


# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#
def print_full_name(first_name, last_name):
    if len(first_name) and len(last_name) <= 10:
        print("Hello" + " " + first_name + " " + last_name + "! You just delved into python.")
        return True

    else:
        return False

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)