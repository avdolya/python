def main():
    pass
name = input()
number = int(input())
group = number // 100
bed = (number // 10) % 10
number_in_group = number % 10
print(f"Группа №{group}.")
print(f"{number_in_group}. {name}.")
print(f"Шкафчик: {number}.")
print(f"Кроватка: {bed}.")
if __name__ == '__main__':
    main()
