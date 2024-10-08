def main():
    ...


def per(a, ss):
    res = ''
    while a != 0:
        res = str(a % ss) + res
        a = a // ss
    return res


mx = 0
res_ss = 0
a = int(input())
for i in range(2, 11):
    if sum(map(int, per(a, i))) > mx:
        mx = sum(map(int, per(a, i)))
        res_ss = i
print(res_ss)
if __name__ == "__main__":
    main()