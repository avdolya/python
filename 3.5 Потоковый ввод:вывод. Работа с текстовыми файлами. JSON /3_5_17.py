from sys import stdin
t = input().lower()
found = False
filename = []
for line in stdin:
    filename.append(line.rstrip("\n"))
for f in filename:
    with open(f, "r", encoding="UTF-8") as file:
        content = file.read()
        content = ' '.join(content.lower().split())
        if t in content:
            found = True
            print(f)
if found == False:
    print('404. Not Found')