import random
import csv
import logger as lg

n = 100
file = open('base_phone.csv', 'w')
newrecord = "ID,Name,Surname,PhoneNumber,email\n"
file.writelines(newrecord)

ls_name = ['John', 'Olga', 'Andrew', 'Ann', 'Michael',
           'Viktor', 'Eduard', 'Alex', 'Mally', 'Igor', 'Gerbert']
ls_surname = ['Cruise', 'Sidez', 'Miles',
              'Gale', 'Shephard', 'Dunes', 'Dime', 'Shananigan', 'True']
ls_e_mail = ['@gmail.com', '@yandex.ru', '@mail.ru']


def list_of_numbers():
    # s = '+'
    randomListPhone = random.randint(79000000000, 80000000000)
    # s = s + str(randomListPhone)
    return str(randomListPhone)


def string_creation():
    s = ""
    s = s + random.choice(ls_name) + ',' + random.choice(ls_surname) + ',' + \
        list_of_numbers() + ',' + random.choice(ls_surname) + random.choice(ls_e_mail)
    return s


def start():
    for i in range(n):
        a = f'{str(i + 1)},{string_creation()}\n'
        file.write(a)
    file.close()


start()
