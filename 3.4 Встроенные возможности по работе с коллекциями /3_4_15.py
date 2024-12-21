from itertools import product, combinations


k = 0
mast = input()
dost = input()
pred = input()
res = []
res_1 = []
arr = ['10', '2', '3', '4', '5', '6', '7', '8', '9', 'валет', 'дама', 'король', 'туз']
arr_2 = ['буби', 'пики', 'трефы', 'черви']
arr_1 = [i for i in arr if i != dost]
a = list(combinations(product(arr_1, arr_2), 3))
for i in a:
    res = []
    res_1 = []
    for j in i:
        res_1 += list(j)
        res.append(' '.join(list(j)))
        
    if mast in res_1:
        res_res = ', '.join(res).replace('буби', 'бубен')
        res_res = res_res.replace('пики', 'пик').replace('трефы', 'треф').replace('черви', 'червей')
        if k == 1:
            print(res_res)
            k = 0

        if res_res == pred:
            k = 1