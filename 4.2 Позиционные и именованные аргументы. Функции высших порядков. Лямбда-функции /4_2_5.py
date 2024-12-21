def to_string(*data, sep=' ',end='\n'):
    return sep.join(map(str, data)) + end 

print(to_string(1, 2, 3))
