def main():
    ...


arr = [i.replace(',', '') for i in input().split()] + [i.replace(',', '') for i in input().split()] 
arr += [i.replace(',', '') for i in input().split()]
arr.sort()
for index, value in enumerate(arr, 1):
    print(f'{index}. {value}')
if __name__ == "__main__":
    main()