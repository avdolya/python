def gcd(a, b):
    k = min(a, b)
    while (a % k != 0) or (b % k != 0):
        k -= 1
    return(k)
print(gcd(144, 96))