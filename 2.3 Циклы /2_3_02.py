def main():
    ...
    

a = input()
k = 0
while a != 'Приехали!':
    if 'зайка' in a:
        k += 1
    a = input()
print(k)
if __name__ == '__main__':
    main()