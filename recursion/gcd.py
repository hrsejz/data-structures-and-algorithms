def gcd(a, b):
    assert int(a) == a and int(b) == b, "The numbers must be integers only"
    if a < 0:
        a = abs(a)
    if b < 0:
        b = abs(b)
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
a = int(input("A: "))
b = int(input("B: "))

result = gcd(a, b)
print(result)