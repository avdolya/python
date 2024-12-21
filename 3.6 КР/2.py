d = dict()
while True:
    line = input().split()
    if not line:
        break
    for word in line:
        last_char = word[-1].upper()
        if word.lower() not in d.get(last_char, []):
            d[last_char] = d.get(last_char, []) + [word.lower()]
for letter in d:
    d[letter].sort()
    d[letter] = ', '.join(d[letter])
    print(f'{letter} - {d[letter]}')