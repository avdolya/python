def main():
    ...


c = 1 
k = 1 
a = int(input())
while k <= a:
    for i in range(c):
        if k > a:
            break
        print(k, end=' ')
        k += 1    
    print()
    c += 1
if __name__ == "__main__":
    main()