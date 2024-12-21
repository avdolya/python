from sys import stdin
lines = []
for line in stdin:
    if line[0] != '#':
        if line.count('#') > 0:
            print((line[:line.find('#')]).strip('\n'))
        else:
            print(line.strip('\n'))
