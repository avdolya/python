def rindex(text):
    a = set()
    d = dict()
    for i in text:
        if i.isalpha():
            a.add(i) 
    for i in a:
        d[i] = text.rfind(i)
    for i in sorted(d.keys()):
        yield (i, d[i])  


text = "The quick brown fox jumps over a lazy dog."
for letter, i in rindex(text):
    print(letter, i, sep="-", end=", ")