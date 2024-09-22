def main():
    pass
n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input()) 
print((m * n - k2 * n) // (k1 - k2), (k1 * n - n * m) // (k1 - k2))
if __name__ == '__main__':
    main()

