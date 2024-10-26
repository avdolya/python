'''def main():
    ...


def factorial(a):
    result = 1
    for i in range(2, a + 1):
        result *= i
    return result


s = input().split()
arr = []
a = b = 0
for i in s:
    if i == '+':
        b = arr.pop()
        a = arr.pop()
        arr.append(a + b)
    elif i == '-':
        b = arr.pop()
        a = arr.pop()
        arr.append(a - b)
    elif i == '*':
        b = arr.pop()
        a = arr.pop()
        arr.append(a * b) 
    elif i == '/':
        b = arr.pop()
        a = arr.pop()
        arr.append(a // b)
    elif i == '~':
        b = arr.pop()
        arr.append(-b)  
    elif i == '!':
        b = arr.pop()
        arr.append(factorial(b)) 
    elif i == '#':
        b = arr.pop()
        arr.append(b)
        arr.append(b)
    elif i == '@':
        c = arr.pop()
        b = arr.pop()
        a = arr.pop()
        arr.append(b) 
        arr.append(c) 
        arr.append(a) 
    else:
        arr.append(int(i))
result = arr.pop()
print(result)
if __name__ == "__main__":
    main()'''
n = int(input())
pred = 0
mx = 0
for i in range(n):
    a = int(input())
    if a < pred and a > mx:
        mx = a
        pred = a
   
print(mx,pred)

