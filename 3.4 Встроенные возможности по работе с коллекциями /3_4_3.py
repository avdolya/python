from itertools import count


def main():
    ...


a = input().split()
for value in count(float(a[0]), float(a[2])):
    if value <= float(a[1]):
        print(f'{value:.2f}')
    else:
        break
if __name__ == "__main__":
    main()