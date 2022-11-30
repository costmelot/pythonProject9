import time
import telepot
from sympy import div
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.loop import MessageLoop
import sympy as sym
from sympy.abc import x

numbers = {}
cnt = 0
flag = 0
result = 1
keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='*', callback_data='2')], [InlineKeyboardButton(text='/', callback_data='1')],
    [InlineKeyboardButton(text='+', callback_data='3')], [InlineKeyboardButton(text='-', callback_data='4')]
])


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    global flag
    global cnt
    global result

    if msg['text'] == '/start':
        bot.sendMessage(chat_id, 'Привет! Это калькулятор полиномов. Введите первый полином в формате '
                                 '5*x**2 - 3*x + 2...')
        flag = 1
        cnt = 0
        return

    numbers[cnt] = msg['text']

    if cnt == 1:
        bot.sendMessage(chat_id, 'Выберите операцию:', reply_markup=keyboard)
        cnt = 0
        result = 0

    if result == 1:
        if flag == 1:
            bot.sendMessage(chat_id, 'Введите второй полином...')
            flag = 0
            cnt = 1
            return

        else:
            bot.sendMessage(chat_id, 'Введите первый полином...')
            flag = 1
            return


def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

    global result
    global numbers

    if query_data == '0':
        bot.sendMessage(from_id, 'Выберите /start чтобы начать снова', reply_markup=keyboard)
        numbers = {}

    elif query_data == '1':
        bot.sendMessage(from_id, 'Результат: ' + '(' + str(numbers[0]) + ')' + ' / ' + '(' + str(numbers[1]) + ')' +
                        ' = ' + str(div((numbers[0]), (numbers[1]))))
        bot.sendMessage(from_id, 'Выберите /start чтобы начать снова')
        result = 1
        numbers = {}

    elif query_data == '2':
        bot.sendMessage(from_id, 'Результат: ' + '(' + str(numbers[0]) + ')' + ' * ' + '(' + str(numbers[1]) + ')' +
                        ' = ' + str(sym.Poly(numbers[0]) * sym.Poly(numbers[1]))[5:-17])
        bot.sendMessage(from_id, 'Выберите /start чтобы начать снова')
        result = 1
        numbers = {}

    elif query_data == '3':
        bot.sendMessage(from_id, 'Результат: ' + '(' + str(numbers[0]) + ')' + ' + ' + '(' + str(numbers[1]) + ')' +
                        ' = ' + str(sym.Poly(numbers[0]) + sym.Poly(numbers[1]))[5:-17])
        bot.sendMessage(from_id, 'Выберите /start чтобы начать снова')
        result = 1
        numbers = {}

    elif query_data == '4':
        bot.sendMessage(from_id, 'Результат: ' + '(' + str(numbers[0]) + ')' + ' - ' + '(' + str(numbers[1]) + ')' +
                        ' = ' + str(sym.Poly(numbers[0]) - sym.Poly(numbers[1]))[5:-17])
        bot.sendMessage(from_id, 'Выберите /start чтобы начать снова')
        result = 1
        numbers = {}
    else:
        bot.sendMessage(from_id, 'Попробуйте еще раз !!!')
        result = 1
        bot.sendMessage(from_id, 'Выберите /start чтобы начать снова')


bot = telepot.Bot('TOKEN')
MessageLoop(bot, {'chat': handle,
                  'callback_query': on_callback_query}).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10)
