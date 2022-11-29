# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import random
# N = int(input('Введие размер списка... '))
# listN = []
# for s in range(N):
#     listN.insert(s, int(random.random() * 10))
# print('Получен список с рандомными числами ==>>',listN)
# sum = 0
# for i in range(N):
#     if i % 2 != 0:
#         sum += listN[i]
#     else:
#         i = i + 1
# print(sum)


# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# import random
# N = int(input('Введие размер списка... '))
# listN = []
# for s in range(N):
#     listN.insert(s, int(random.random() * 10))
# print('Получен список с рандомными числами ==>>', listN)
# listSum = []
# for i in range(len(listN)):
#     while i < len(listN)/2 and N > len(listN)/2:
#         N = N - 1
#         S = listN[i] * listN[N]
#         listSum.append(S)
#         i += 1
# print('Получен список с перемноженными парами числами ==>>', listSum)

# 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import random
# N = int(input('Введие размер списка... '))
# listN = []
# for s in range(N):
#     listN.insert(s, round(random.random() * 10, 2))
# print('Получен список с рандомными числами ==>>', listN)

# maxIndex = listN[0]
# minIndex = listN[0]
# for i in listN:
#     if maxIndex < listN.index(str.split(i)[1][0][1]):
#         maxIndex = listN.index(str.split(i))
#     else:
#         i += 1
# for i in listN:
#     if minIndex > listN.index(str.split(i)[1][0][1]):
#         minIndex = listN.index(str.split(i))
#     else:
#         i += 1
# print(maxIndex)
# print(minIndex)
# print(maxIndex+minIndex)

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


N = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
S = ""
while N != 0:
    S = str(N % 2) + S
    N //=2
print(S)
        



# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]