dict = {}
arr = []
food = []
k = 0
n = int(input())  #кол-во ингредиентов
for i in range(n):
    food.append(input())
m = int(input())  #кол-во рецептов
for i in range(m):
    a = input()  #название блюда
    b = int(input())  #кол-во ингредиентов
    for j in range(b):
        ingr = input()
        if ingr in food:
            k += 1
    if k == b:
        arr.append(a)
    k = 0
if len(arr) != 0:
    for i in sorted(arr):
        print(i)
else:
    print('Готовить нечего')
