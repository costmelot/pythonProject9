from datetime import datetime


def LOG(func):
    def wrapper(*args):
        func(*args)
        with open('log.csv', 'a', encoding='utf-8') as log:
            log.write(f'Была запущена функция {func.__name__} {func.__doc__} {datetime.now()}\n')

    return wrapper
