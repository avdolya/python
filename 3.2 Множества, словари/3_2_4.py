set_1 = set()
set_2 = set()
n = int(input()) 
m = int(input())    
for i in range(n):
    a = input()
    set_1.add(a)
for i in range(m): 
    a = input()
    set_2.add(a)
set_res = set_1 & set_2
if len(set_res) == 0:
    print('Таких нет')
else:
    print(len(set_res))
