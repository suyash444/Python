def swap_case(s):
    if 0 < len(s) <= 1000:
        return s.swapcase()


s = input("Enter the String:")
result = swap_case(s)
print(result)
swap_case(s)