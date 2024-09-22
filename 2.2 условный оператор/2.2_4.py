def main():
    pass
p = int(input())
v = int(input())
t = int(input())
if p < v < t:
    print(f'1. Толя')
    print(f'2. Вася')
    print(f'3. Петя')
if t < v < p:
    print(f'1. Петя')
    print(f'2. Вася')
    print(f'3. Толя')
if v < p < t:
    print(f'1. Толя')
    print(f'2. Петя')
    print(f'3. Вася')
if t < p < v:
    print(f'1. Вася')
    print(f'2. Петя')
    print(f'3. Толя')
if p < t < v:
    print(f'1. Вася')
    print(f'2. Толя')
    print(f'3. Петя')
if v < t < p:
    print(f'1. Петя')
    print(f'2. Толя')
    print(f'3. Вася')
if __name__ == '__main__':
    main()
