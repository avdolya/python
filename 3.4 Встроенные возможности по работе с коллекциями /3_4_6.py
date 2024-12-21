from itertools import product


def main():
    ...


a = input()
mast = ['пик', 'треф', 'бубен', 'червей']
arr = [i for i in mast if i != a]
values = list(product(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз'], arr))
for value in values:
    print(f'{value[0]} {value[1]}')

if __name__ == "__main__":
    main()