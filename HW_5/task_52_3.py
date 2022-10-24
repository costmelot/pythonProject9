# Создайте программу для игры с конфетами против бота с "интеллектом"

import random


def start():
    print(f'################## Игра "2021 конфета" ##################')
    print(f'Всего на столе 2021 конфета')
    print(f'Каждый игрок по очереди берет от 1 до 28 конфет')
    print(f'Выигрывает тот, кто заберет последние конфеты со стола!')
    print(f'######################################################\n')


def rnd_turn():
    print(f'Выбор очередности ходов: ')
    print(f'Введите 0, если ходить первым будет игрок')
    print(f'Введите 1, если ходить первым будет компьютер')
    print(f'Введите 2, чтобы выбрать очередность ходов случайным образом')
    while True:
        n = input('> ')
        if n.isdigit():
            n = int(n)
            if n > 2 or n < 0:
                print(f'Введите число 0, 1 или 2')
            else:
                if n == 2:
                    n = random.randint(0, 1)
                if n == 0:
                    print(f'Первым будет ходить игрок!')
                else:
                    print(f'Первым будет ходить компьютер!')
                break
        else:
            print(f'Вы ввели недопустимый символ. Введите число 0, 1 или 2')
    return n


def turn_player(candys):
    n = 29
    while n > 28 or n < 1:
        n = input('Сколько вы возьмете конфет? ')
        if n.isdigit():
            n = int(n)
            if n > 28 or n < 1:
                print(f'Вы вязли недопустимое количество конфет! Возьмите от 1 до 28')
            if n > candys:
                print(f'Вы взяли больше чем осталось конфет!')
                n = 29
        else:
            print(f'Вы ввели недопустимые символы. Введите число от 1 до 28')
            n = 29
    return n


# Функция хода компьютера с выигрышной стратегией
def turn_ai(candys):
    n = candys % 29
    if n == 0:
        n = random.randint(1, 28)
    return n


candys = 2021
count = 1
start()
turn = rnd_turn()
while True:
    print(f'\n******** Ход номер: {count} ********')
    if turn % 2 == 0:
        print(f'Ход игрока! Всего конфет: {candys}')
        n = turn_player(candys)
        print(f'Игрок взял конфет: {n}')
    elif turn % 2 == 1:
        print(f'Ход компьютера! Всего конфет: {candys}')
        n = turn_ai(candys)
        print(f'Компьютер взял конфет: {n}')
    candys -= n
    if candys == 0:
        if turn % 2 == 0:
            print(f'Победил игрок!')
        else:
            print(f'Победил компьютер!')
        break
    turn += 1
    count += 1

print('\n' * 5)
