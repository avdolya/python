from itertools import product


def main():
    ...


n = input()
b = set()
for i in n:
    if i.isupper():
        b.add(i)
res = sorted(list(b))
print(' '.join(res) + ' F')
a = list(product([0, 1], repeat = len(res)))
for values in a:
    variables = {res[j]: values[j] for j in range(len(res))}
    result = int(eval(n, {}, variables))
    print(' '.join(map(str, list(values))), int(result))
if __name__ == "__main__":
    main()