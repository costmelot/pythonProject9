# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

n = int(input("Введите натуральное число: "))
list1 = []
d = 2
m = n
while d * d <= n:
    if n % d == 0:
        list1.append(d)
        n //= d
    else:
        d += 1
list1.append(n)
print('{} = {}'.format(m, list1))
