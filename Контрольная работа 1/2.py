a = int(input())
b = int(input())
oper = input()
if len(oper) % 6 == 0:
    print(a + b)
elif len(oper) % 3 == 0:
    print(a - b)
elif len(oper) % 2 == 0:
    print(a * b)
else:
    print(a // b)