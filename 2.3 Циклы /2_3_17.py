def main():
    ...


a = input()
st = ''
for i in range(len(a)):
    if int(a[i]) % 2 != 0:
        st += a[i]
    else:
        ...  
print(st)   
if __name__ == "__main__":
    main()
