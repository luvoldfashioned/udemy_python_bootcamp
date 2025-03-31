list_of_strings = input().split(',')
# TODO: Use list comprehension to convert the strings to integer
str_conv_int = [int(s) for s in list_of_strings]

# TODO: Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"
result = [n for n in str_conv_int if n % 2 == 0]

print(result)
