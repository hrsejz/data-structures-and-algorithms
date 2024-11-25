def decimalToBinary(n):
    if n == 0:
        return 0
    else:
        return n%2 + 10*decimalToBinary(n//2)

print(decimalToBinary(5))
print(type(decimalToBinary(6)))

# def decimal_to_binary(n):
#     if n == 0:
#         return "0"  # Base case for 0
#     elif n == 1:
#         return "1"  # Base case for 1
#     else:
#         return decimal_to_binary(n // 2) + str(n % 2)
    
# print(decimal_to_binary(13))
# print(type(decimal_to_binary(13)))