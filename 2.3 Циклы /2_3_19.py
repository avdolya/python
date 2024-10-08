def main():
    ...


second = 1001
first = 0
b = ''
print((first + second) // 2)
b = input()
while b != 'Угадал!':
    if b == 'Меньше':
        second = (first + second) // 2
        print((first + second) // 2)
    else:
        first = (first + second) // 2
        print((first + second) // 2)  
    b = input()
if __name__ == "__main__":
    main()
               
               
          