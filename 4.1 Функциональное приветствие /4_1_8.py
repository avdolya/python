def is_palindrome(x):
    if isinstance(x,int) or isinstance(x,float):
        test = str(abs(x))
    if test[::-1] == x:
        return True
    else:
        return False
print(is_palindrome([1, 2, 1, 2, 1]))
