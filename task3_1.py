#     1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#     Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

size = int(input('Введите размер списка '))
lst = []
sum = 0
for i in range(size):
   
    lst.append(randint(0, 9))
    if i % 2 != 0:
        sum += lst[i]


print(lst)
print(f'Сумма элементов списка на нечетных позициях равна {sum}')