def main():
    ...


a = input().split(' ')
st = int(input())
print(*(int(i) ** st for i in a))
if __name__ == "__main__":
    main()