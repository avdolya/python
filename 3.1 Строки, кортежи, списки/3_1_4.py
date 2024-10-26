def main():
    ...


a = 'afdgvfg333'
while a != ' ':
    a = input()
    if a[-3:] == '@@@':
        ...
    elif a[:2] == '##':
        print(a[2:])
    else:
        print(a)
if __name__ == "__main__":
    main()