############ factorial ############ 4! = 4.3.2.1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
n = int(input("Enter number to get factorial: "))
result = factorial(n)
print(f"{n}! = {result}")

#################################3

# def first_method():
#     second_method()
#     print("I'm the first method")
# def second_method():
#     third_method()
#     print("I'm the second method")
# def third_method():
#     fourth_method()
#     print("I'm the third method")
# def fourth_method():
#     print("I'm the fourth method")
    
# first_method()

############ 2^n ############

# def power_of_two(n):
#     if n == 0:
#         return 1
#     else:
#         power = power_of_two(n-1)
#         return power * 2

# def power_of_two(n):
#     power = 1
#     i = 0
#     while i < 3:
#         power = power * 2
#         i = i + 1
#     return power
    
# result = power_of_two(3)
# print(result)

#### Russian Doll recursive function ###

def openRussianDoll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        openRussianDoll(doll-1)


openRussianDoll(4)