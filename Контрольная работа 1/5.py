n = int(input())
a = ''
res_sum = 0
sm = k = 0
for i in range(n):
    while ((a := input()) != 'stop'):
        sm += int(a)
        k += 1
    res_sum += sm / k
    sm = k = 0
print(f'{res_sum:.2f}')
