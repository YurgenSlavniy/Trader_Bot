import sys
from time import sleep  
from tblib.lib import (
    isvalid_pair, set_status, trim_tail, 
    calculate_buy, calculate_sell, print_info, 
    print_buy_info, print_sell_info,
    print_currency_list, TraderBotException
)

bad_text = ''
bad_num  = 0

pairs = [
    'EXM/RUB',  'SMART/RUB', 'XRP/RUB',
    'ALGO/RUB', 'BTT/RUB',   'DAI/RUB',
    'ONG/RUB',  'ONT/RUB',   'TRX/RUB',
    'USDT/RUB', 'XLM/RUB',   'LSK/RUB',
]

user_info = {
    'pair_name':    '',
    'currency':     '',    # покупаемая крипто-валюта
    'use_currency': '',    # валюта для покупки крипто-валюты
    'ratio_price': {       # соотношение цен
        'buy':  0,
        'sell': 0,
    },    
    'status':       '',    # статус пользователя
    'balance':          0, # баланс
    'order_size':       0, # размер одного ордера
    'current_price':    0, # текущая цена валюты
    'min_price':        0, # минимальная граница цены
    'max_price':        0, # максимальная граница цены
    'comission':        0, # комиссия
    'total_orders':     0, # общее колличество ордеров
    'price':            0, # общая цена без комиссии
    'real_price':       0, # общая цена + комиссия
    'order_price':      0, # цена одного ордера без комиссии
    'real_order_price': 0, # цена одного ордера + комиссия
    'profit':           0, # профицит от продажи
}

msg = """
 Привет, Я финансовый помошник. 
 Kоторый поможет сгенерировать ордера для биржи криптовалют.

 Для генерации ордеров необходимо будет ввести запрашиваемые
 программой данные.

 1) Название торговый пары
 2) Сколько вы готовы инвестировать в рублях
 3) Биржевой курс на данный момент времени
 4) Минимальную цену покупки
 5) Максимальную цену продажи
 6) Выбирите соотношение BUY/SELL 0/0
 7) Минимальный ордер
"""
print(msg)
print_currency_list(pairs, 5)

print('\n Введите данные в одну строку через пробел:\n')

options = input(' > ').split()

# ввод пары
pair_name = options.pop(0).strip().upper()

if isvalid_pair(pair_name) and pair_name != bad_text:
    val = pair_name.split('/')

    user_info['pair_name']    = pair_name
    user_info['currency']     = val[0]
    user_info['use_currency'] = val[1]

    if pair_name not in pairs:
        pairs.append(pair_name)
else:
    raise TraderBotException('Формат введенной пары не корректен')
# конец ввода пары

# ввод баланса
balance = int(options.pop(0))

user_info['status'] = set_status(balance)

if balance <= bad_num:
    raise TraderBotException('Баланс должен быть больше ' + bad_num)
else:
    user_info['balance'] = balance
# конец ввода баланса

# ввод текущей цены
current_price = float(options.pop(0))

if current_price <= bad_num:
    raise TraderBotException('Цена должна быть больше ' + bad_num)
else:
    user_info['current_price'] = current_price
# конец ввода текущей цены

min_price = float(options.pop(0))
if min_price <= bad_num:
    raise TraderBotException('Минимальная граница должна быть больше ' + bad_num)
else:
    user_info['min_price'] = min_price


max_price = float(options.pop(0))
if max_price <= bad_num:
    raise TraderBotException('Максимальная граница должна быть больше ' + bad_num)
else:
    user_info['max_price'] = max_price

# ввод соотношения цен
ratio_price = options.pop(0)

arr = ratio_price.split('/')

buy  = int(arr[0])
sell = int(arr[1])

# if buy == bad_num or sell == bad_num:
#     raise TraderBotException(f'Соотношение цен не корректно {buy}/{sell}')

user_info['ratio_price'] = {
    'buy': user_info['balance'] * (buy / 100),
    'sell':user_info['balance'] * (sell / 100),
}
# конец соотношения цен

# ввод минимальный размер ордера
order_size = int(options.pop(0))

if order_size <= bad_num:
    raise TraderBotException('Размер ордера должен быть больше ' + bad_num)
else:
    user_info['order_size'] = order_size
# конец минимальный размер ордера

# ввод комиссии
user_info['comission'] = 0
# конец ввода комиссии

print('\n Будет произведена генерация ордеров для торговой пары {}\n'
      ' Ваш баланс {} RUB\n'
      ' рыночная цена {} {}\n'
      ' Ордера будут сгенерированы на участке цены от {} до {}\n'
      .format(pair_name, balance, current_price, user_info['use_currency'], min_price, max_price)
)

str = '.'
print(' Подождите ', end='')
sys.stdout.flush()
for i in range(11):
    sleep(1)
    print(str, end='')
    sys.stdout.flush()

print('\n\n')
# emx/rub 10000 10 1 20 40/60 10
if int(user_info['ratio_price']['buy']):
    print('*' * 80)
    calculate_buy(user_info)
    print_buy_info(user_info)

print('*' * 80)

if int(user_info['ratio_price']['sell']):
    calculate_sell(user_info)
    print_sell_info(user_info)
    print('*' * 80)


for key in user_info:
    print('', key, ':', user_info[key])
# print_currency_list(currency_list)