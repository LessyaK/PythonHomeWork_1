# 5 Реализуйте алгоритм перемешивания списка 

n = int(input('Введите размерность списка: '))
d_min = int(input('Введите минимальное число в диапазоне: '))
d_max = int(input('Введите максимальное число в диапазоне: '))

import random
list = [random.randint(d_min,d_max) for i in range(1,n+1)]
print(f"исходный список:\n {list}")
random.shuffle(list)
print(f"список после перемешивания:\n{list}")
