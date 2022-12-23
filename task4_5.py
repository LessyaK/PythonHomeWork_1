# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('poly_1.txt', 'w' , encoding='utf-8') as file:
    file.write('4*x^3 + 5*x^2 + 10*x + 6')
with open('poly_2.txt', 'w', encoding='utf-8') as file:
    file.write('15*x^2 + 3')

with open('poly_1.txt','r') as file:
    poly_1 = file.readline()
    print(f'Многочлен 1: ({poly_1})')

with open('poly_2.txt','r') as file:
    poly_2 = file.readline()
    print(f'Многочлен 2: ({poly_2})')

print(f'Сумма многочленов ({poly_1} + {poly_2})')


with open('sum_poly.txt', 'w', encoding='utf-8') as file:
    file.write(f'{poly_1} + {poly_2}')