# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр

n = input('Введите число: ')

sum = 0

for digit in n:
    if digit.isdigit():
        sum += int(digit)

print("Сумма:", sum)
