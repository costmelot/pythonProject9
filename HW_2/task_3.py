# Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

n = int(input('Введите количество чисел в последовательности: '))

numbers = []

for i in range(1, n + 1):
    value = (1 + 1 / i) ** i
    numbers.append(value)

sum = 0
for i in numbers:
    sum += i

print('Сумма всех чисел последовательности:', sum)
