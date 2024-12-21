
a = input()
b = input()
c = input()
s1 = []
s2 = []
res = []
with open(a) as file_in_1:
    s1 = set([line for line in file_in_1.read().split()])
with open(b) as file_in_2:
    s2 = set([line for line in file_in_2.read().split()])
u = s1 ^ s2
with open(c, "w", encoding="UTF-8") as file_out:
    for i in sorted(u):
        file_out.writelines(i + '\n')