#  Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.


import re
from sympy import Symbol, collect


def convert(line):
    line = re.sub(r'(\d)(x)', r'\1*\2', line)
    line = line.replace('^', '**')
    line = line[:-4:]
    return line


with open('file1.txt', 'r') as data1:
    record1 = data1.readline()

with open('file2.txt', 'r') as data2:
    record2 = data2.readline()

print(f'Многочлен из первого файла: {record1}')
print(f'Многочлен из второго файла: {record2}')

record1 = convert(record1)
record2 = convert(record2)

x = Symbol('x')

result = str(collect(record1 + ' + ' + record2, x))
result = result.replace('**', '^')
result = result.replace('*', '')
result = result + ' = 0'
print(f'Сумма многочленов: {result}')

with open('file3.txt', 'w') as data3:
    data3.write(result)
