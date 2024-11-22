# sum of digits of 123 = 1 + 2 + 3 = 6

########### Recursive Solution Using Maths ###########

def sum_of_digits(n):
    """
    This function calculates the sum of digits of a given integer `num` recursively.
    F(n) = (n % 10) + F(n / 10)
    """
    assert n >= 0 and int(n) == n, "Input must be a non-negative integer."
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)
    
n = int(input("Enter an integer: "))
result = sum_of_digits(n)
print(f"The sum of the digits is: {result}")

########### Recursive Solution Using Strings ###########

# def sum_of_digits(integer):
#     # Base case: when the string has only one character, return that integer as the result
#     if len(integer) == 1:
#         return int(integer[0])
#     else:
#         # Recursive case: sum the first digit and call the function on the rest of the string
#         return int(integer[0]) + sum_of_digits(integer[1:])
# user_input = input("Enter an integer: ")
# result = sum_of_digits(user_input)
# print(f"The sum of the digits is: {result}")


########### Iterative Solution ###########

# def sum_of_digits(integer):
#     sum = 0
#     for _ in integer:
#         sum += int(_)
#     return sum

# integer = input("Enter a number to get the sum of its digits: ")
# result = sum_of_digits(integer)
# print(f"Sum of the digits of {integer} = {result}")