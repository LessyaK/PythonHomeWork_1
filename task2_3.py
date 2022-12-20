# 3 Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму 

# *Пример:*

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Введите число n: '))
list = [round((1+1/i)**i, 3) for i in range(1, n+1)]

summ = 0
for j in range(0,n):
       summ += list[j]
print(f'Последовательность: {list}\nСумма: {round(summ, 3)}')


# вар 2
# n = int(input('Priny your N: '))
# my_dict = {}
# for i in range(1,n+1):
#     my_dict[i] = (1+1/i)**i
#     my_dict[i] = round(my_dict[i],2)
# print(my_dict)



# print('Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.')
# n = int(input('Введите число N:-> '))
# seq = dict()
# seq_sum = 0
# for i in range(1, n+1):
#     seq[i] = round((1+1/i)**i, 2)
# print(f'Для N={n} {seq}')
# print(f'Сумма {sum(seq.values())}')
