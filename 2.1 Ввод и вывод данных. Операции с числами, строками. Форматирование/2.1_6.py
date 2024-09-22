def main():
    pass
name = input()
price = int(input())
weight = int(input())
kol = int(input())
print("Чек")
print(f"{name} - {weight}кг - {price}руб/кг")
print(f"Итого: {price * weight}руб")
print(f"Внесено: {kol}руб")
print(f"Сдача: {kol - price * weight}руб")

if __name__ == '__main__':
    main()
