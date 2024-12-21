a = input().split()
print('[')
for i in a:
    print('{')
    print(f' "digits": {len(bin(int(i))[2:])},')
    print(f' "units": {bin(int(i))[2:].count('1')},')
    print(f' "zeros": {bin(int(i))[2:].count('0')}')
    if i == a[len(a) - 1]:
        print('}')
    else:
        print('},')    
print(']') 
