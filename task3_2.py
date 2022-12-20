# 2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

size = int(input('Введите размер списка '))
list_old = []
list_new = []

for i in range(size):
    list_old.append(randint(0, 9))

for i in range(len(list_old)):
    while i < len(list_old)/2 and size > len(list_old)/2:
        size = size - 1
        x = list_old[i] * list_old[size]
        list_new.append(x)
        i += 1

print(f'{list_old}', '=>', f'{list_new}')
