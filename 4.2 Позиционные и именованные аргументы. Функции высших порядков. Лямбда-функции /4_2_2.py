def make_matrix(size, value=0):
    if isinstance(size,tuple):
        width, height = size
    else:
        width = height = size
    return [[value for i in range(width)] for j in range(height)]


print(make_matrix((4, 2), 1))
