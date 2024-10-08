def main():
    ...


sm = 0
t = float(input())
while t != 0:
    if t >= 500:
        sm += t * 0.9
    else:
        sm += t
    t = float(input())
print(sm)
if __name__ == "__main__":
    main()