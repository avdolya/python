def main():
    ...


n = int(input())
for i in range(n):
    a = input()
    ind = a.find('зайка')
    if ind != -1:
        print(ind + 1)
    else:
        print('Заек нет =(')
if __name__ == "__main__":
    main()