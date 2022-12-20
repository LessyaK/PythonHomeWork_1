# 3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


from random import uniform


size = int(input('Введите размер списка: '))
list1 = []
for i in range(size):
    f = uniform(0, 9)
    list1.append(round(f, 2))
print(f'Исходный список: {list1}')

new_lst = [round(i%1,2) for i in list1 if i%1 != 0]
# print(max(new_lst) - min(new_lst))
print(f'Cписок из дробных частей исходного списка: {new_lst}')
print(f'max дробная часть = : {max(new_lst)}, min дробная часть = : {min(new_lst)} ')

delta = round(max(new_lst) - min(new_lst),2)
print(f'Разницa между максимальным и минимальным значением дробной части элементов = ', delta)