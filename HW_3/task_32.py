# 32. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

from random import randint

n = int(input('Введите количество элементов в списке:\n'))

numbers = [randint(-n, n) for i in range(n)]
print('Вот Ваш список:\n', numbers)

l = len(numbers) // 2 + 1 if len(numbers) % 2 != 0 else len(numbers) // 2
new_lst = [numbers[i] * numbers[len(numbers) - i - 1] for i in range(l)]
print('Произведение пар чисел списка:\n', new_lst)
