import os
n = 0
size = os.path.getsize('/Users/olaavduhina/Desktop/lms/3.5 Потоковый ввод:вывод. Работа с текстовыми файлами. JSON /a.txt')
arr = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
while size > 1024 and n < len(arr):
    n += 1
    size = size // 1024
    if size % 1024 != 0:
        size += 1

print(f'{size}{arr[n]}')
