def power(b, x):
    assert x >= 0 and int(x) == x, "Exponent must be a non-negative integer."
    if x == 0:
        return 1
    else:
        return b * power(b, x - 1)

b = int(input("Base: "))
x = int(input("Exponent: "))
result = power(b, x)
print(result)

# def power_of_two(x):
#     if x == 0:
#         return 1
#     else:
#         power = power_of_two(x-1)
#         return power * 2