# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


dbl = ""
dec = int(input('Введите десятичное число: '))
while dec != 0:
    dbl = str(dec % 2) + dbl
    dec //=2
print(f'Двоичное число = {dbl}')