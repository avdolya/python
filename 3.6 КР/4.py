from itertools import product
n = int(input())
d = []
for i in range(n):
    line = input().strip()
    d.append(line.split(', '))
unique_numbers = set()

for length in range(n):
    for i in product(*[d[i] for i in range(n)]):
        number = ''.join(i)
        unique_numbers.add(int(number))  
for number in sorted(unique_numbers):
    print(number)