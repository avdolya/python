def main():
    ...


ln = int(input())
for i in range(n := int(input())):
    a = input()
    if len(a) > ln:
        print(f"{a[:-(len(a) - ln + 3)]}...")  
    else:
        print(a)    
if __name__ == "__main__":
    main()