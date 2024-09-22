def main():
    pass
hours = int(input())
min = int(input())
t = int(input())
if min + t < 60:
    if hours >= 24:
        hours = hours - (hours // 24) * 24
    print(f'{str(hours):0>2}:{str(min + t):0>2}')
elif min + t >= 60:
    hours = hours + (min + t) // 60
    min = min + t - ((min + t) // 60) * 60
    if hours >= 24:
        hours = hours - (hours // 24) * 24
    print(f'{str(hours):0>2}:{str(min):0>2}')
if __name__ == '__main__':
    main()
