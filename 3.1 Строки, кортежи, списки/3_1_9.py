def main():
    ...


while (a := input()):
    if a[0] != '#':
        if '#' in a:
            ind = a.index('#')
            print(a[:ind])
        else:
            print(a)
if __name__ == "__main__":
    main()