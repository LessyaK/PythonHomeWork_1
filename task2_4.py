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



# вар 2
# >>> f = open('xyz.txt','w')  # открытие в режиме записи
# >>> f.write('Hello \n World')  # запись Hello World в файл
# Hello
# World
# >>> f.close()  # закрытие файла

# pos = open('file.txt', 'w')
# pos.write('{}\n'.format(a))
# pos.write('{}\n'.format(b))
# pos.write('{}\n'.format(c))
# pos.close()


# import random

# num = int(input("Ведите число: "))  # = 5
# my_list = []
# for i in range(num):
#     my_list.append(random.randint(-num, num))
# print(my_list)
# # делали так на 1й задаче 2го семинара

# path = 'file.txt'
# data = open(path, 'w')
# data.write('2\n')
# data.write('4\n')
# data.close()

# path = 'file.txt'
# data = open(path, 'r')
# mult = 1
# for line in data:
#     mult*=my_list[int(line)]
#     # print(line, end='')
# print(mult)
