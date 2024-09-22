def main():
    pass
name = input()
price = int(input())
weight = int(input())
money = str(int(input()))
s = str(int(money) - weight * price)
result = f'{weight}кг * {price}руб/кг'
price_res = str(weight * price)
print('================Чек================')
print(f'Товар:{name.rjust(29)}')
print(f'Цена:{result.rjust(30)}')
print(f'Итого:{price_res.rjust(26)}руб')
print(f'Внесено:{money.rjust(24)}руб')
print(f'Сдача:{s.rjust(26)}руб')
print('===================================')
if __name__ == '__main__':
    main()

