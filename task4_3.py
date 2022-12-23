# 3.Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

size = int(input('Введите размер списка '))
lst_old = []
for i in range(size):
    lst_old.append(randint(0, 20))
print(f"Исходный список: {lst_old}")

lst_new = []
[lst_new.append(i) for i in lst_old if i not in lst_new]
print(f"Список из неповторяющихся элементов: {lst_new}")