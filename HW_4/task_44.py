# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x^2 = 0

from random import randint

max_val = 100
k = int(input('Введите натуральную степень k: '))

ratio = [randint(0, max_val) for i in range(k)] + [randint(1, max_val)]
polynom = '+'.join([f'{(j, "")[j == 1]}x^{i}' for i, j in enumerate(ratio) if j][::-1]) + " = 0"

polynom = polynom.replace('x^1+', 'x+')
polynom = polynom.replace('x^0', '')
polynom += ('', '1')[polynom[-1] == '+']
polynom = (polynom, polynom[:-2])[polynom[-2:] == '^1']

with open('file.txt', 'w') as data:
    data.write(polynom)
