def recursive_digit_sum(a):
    if len(str(a)) == 0:
        return 0
    return int(str(a)[0]) + recursive_digit_sum(str(a)[1:len(str(a))])
print(recursive_digit_sum(123))