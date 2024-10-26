def main():
    ...


a = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
n = int(input())
for i in range(n):
    print(a[i % len(a)])
if __name__ == "__main__":
    main()