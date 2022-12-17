# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

def list(n):
    list = []
    for i in range(n):
        list.append(randint(-n, n))
    return list


n = int(input('Введите число N: '))
numbers = list(n)
print(numbers)

p1 = int(input(f'Введите позицию 1 в диапазоне от 0 до {n-1}: ')) 
p2 = int(input(f'Введите позицию 1 в диапазоне от 0 до {n-1}: ')) 
if (p1 or p2) < 0 or (p1 or p2) > (n-1):
    print('Некорректный номер позиции')
else:
    print(f'Произведение позиции: {numbers[p1]} и {numbers[p2]} = {numbers[p1]*numbers[p2]}')

