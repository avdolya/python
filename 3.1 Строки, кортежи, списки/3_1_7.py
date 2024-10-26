def main():
    ...


a = input()
sm = 0
a = a.split(' ')
for i in a:
    sm += int(i)
print(sm)
if __name__ == "__main__":
    main()