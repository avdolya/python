def main():
    pass
p = 43872 / int(input()) 
v = 43872 / int(input())
t = 43872 / int(input())
if p < v < t:
    print('Петя')
if t < v < p:
    print('Толя')
if v < p < t:
    print('Вася')
if t < p < v:
    print('Толя')
if p < t < v:
    print('Петя')
if v < t < p:
    print('Вася')
if __name__ == '__main__':
    main()
