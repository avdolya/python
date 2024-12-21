n = int(input())
for i in range(n):
    s = input().split('&')
    print(s[2][int(s[0]):int(s[0]) + int(s[1]) * 2:2])
