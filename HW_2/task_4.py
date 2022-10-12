# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов
# на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

n = int(input('Введите количество элементов в списке:\n'))
numbers = [randint(-n, n) for i in range(n)]
print(numbers)

with open("file.txt", 'w') as data:
    data.write('1\n')
    data.write('3\n')
    data.write('4\n')

data = open("file.txt", 'r')
data_list = [int(line.strip()) for line in data]
data.close()

multiplication = 1
for i in data_list:
    multiplication *= numbers[i]
print(f'Произведение элементов списка: {multiplication}')
