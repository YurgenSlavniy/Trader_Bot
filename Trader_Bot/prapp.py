
from tblib.lib import (
    isvalid_pair, set_status, trim_tail, 
    calculate_buy, calculate_sell, print_info, 
    print_buy_info, print_sell_info,
    print_currency_list, TraderBotException
)

bad_text = ''
bad_num  = 0

currency_list = {
    'EMX': 10, 'XRP': 20, 'DAI': 30, 'XLM': 40,
    'LSK': 50, 'ONG': 60, 'ONT': 70, 'TRX': 80,
}

user_info = {
    'pair_name':    '',
    'currency':     '',    # покупаемая крипто-валюта
    'use_currency': '',    # валюта для покупки крипто-валюты
    'action':       '',    # действие пользователя
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
 ПРИВЕТ, Я ФИНАНСОВЫЙ ПОМОШНИК.

 Для генерации ордеров необходимо ввести:
  1) Название торговой пары EMX/RUB.
  2) Сколько вы готовы инвестировать в валюту.
  3) Тип производимой операции buy/sell.
  4) Биржевую цену на данный момент.
  5) Количество криптовалюты в одном ордере:
        *количество приведенно в списке валют
        *оставить по умолчанию Enter
        *для изменения ввести новое количество
        *если валюты нет в списке, обязательно ввести количество
  6) Комиссию.
  7) Нижнюю или верхнюю границу цены.
"""
print(msg)

# print_currency_list не владеет -> currency_list
print_currency_list(currency_list)

# ввод пары
pair_name = input('\n 1) Пара: ').strip().upper() or bad_text

if isvalid_pair(pair_name) and pair_name != bad_text:
    val = pair_name.split('/')

    user_info['pair_name']    = pair_name
    user_info['currency']     = val[0]
    user_info['use_currency'] = val[1]

    if user_info['currency'] not in currency_list:
        currency_list[user_info['currency']] = 0
else:
    raise TraderBotException('Формат введенной пары не корректен')
# конец ввода пары

# ввод баланса
balance = int(input(' 2) Сумма: ') or bad_num)

user_info['status'] = set_status(balance)

if balance != bad_num:
    user_info['balance'] = balance
else:
    raise TraderBotException('Баланс должен быть больше ' + bad_num)
# конец ввода баланса

# ввод действия
action = input(' 3) Действие: ').strip().lower() or bad_text

if action == 'sell' or action == 'buy' and action != bad_text:
    user_info['action'] = action
else:
    raise TraderBotException('Тип проиводимой операции не корректен ' + action)
# конец ввода действия

# ввод текущей цены
current_price = float(input(' 4) Цена: ') or bad_num)

if current_price != bad_num:
    user_info['current_price'] = current_price
else:
    raise TraderBotException('Цена должна быть больше ' + bad_num)
# конец ввода текущей цены

# ввод оличества криптовалюты
order_size = int(input(' 5) Количество: ') or bad_num)

if order_size != bad_num:
    currency_list[user_info['currency']] = order_size
    user_info['order_size']              = order_size
else:
    order_size = currency_list[user_info['currency']]
    user_info['order_size'] = order_size
# конец ввода оличества криптовалюты

# ввод комиссии
comission = float(input(' 6) Комиссия: ') or 0)

if comission != bad_num:
    user_info['comission'] = comission
else:
    raise TraderBotException('Комиссия должна быть больше ' + bad_num)
# конец ввода комиссии

if user_info['action'] == 'buy':
    min_price = float(input(' 7) Минимальная цена: ') or bad_num) # ?
    if min_price != bad_num:
        user_info['min_price'] = min_price
    else:
        raise TraderBotException('Минимальная граница должна быть больше ' + bad_num)

if user_info['action'] == 'sell':
    max_price = float(input(' 7) Максимальная цена: ') or bad_num) # ?
    if max_price != bad_num:
        user_info['max_price'] = max_price
    else:
        raise TraderBotException('Максимальная граница должна быть больше ' + bad_num)

# вывод информации
# print_info не владеет -> user_info
print_info(user_info)

if user_info['action'] == 'buy':
    # calculate_buy владеет -> user_info
    calculate_buy(user_info)
    # print_buy_info не владеет -> user_info
    print_buy_info(user_info)

if user_info['action'] == 'sell':
    # calculate_sell владеет -> user_info
    calculate_sell(user_info)
    # print_sell_info не владеет -> user_info
    print_sell_info(user_info)


# for key in user_info:
#     print('', key, ':', user_info[key])
# print_list(currency_list)