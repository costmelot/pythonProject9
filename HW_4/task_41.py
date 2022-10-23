# Задача №30: Вычислить число c заданной точностью d. Пример:
# при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10)

from decimal import Decimal

a = input('Введите число: ')
d = input('Введите заданную точность: ')

num = Decimal(a)
num = num.quantize(Decimal(d))
print(f'Число {a} с заданной точностью {d} равно {num}')
