
from tblib.lib import (
    isvalid_pair, print_list, detect_status, 
    trim_tail, calculate_buy, calculate_sell,
    TraderBotException
)

bad_text = ''
bad_num  = 0

list_currency = {
    'EMX': 10, 'XRP': 20, 'DAI': 30, 'XLM': 40,
    'LSK': 50, 'ONG': 60, 'ONT': 70, 'TRX': 80,
}

user_info = {}

msg = """
 ПРИВЕТ, Я ФИНАНСОВЫЙ ПОМОШНИК.

 Для генерации ордеров необходимо ввести:
  1) Название торговой пары EMX/RUB
  2) Сколько вы готовы инвестировать в валюту
  3) Тип производимой операции buy/sell
  4) Биржевую цену на данный момент
  5) Количество криптовалюты в одном ордере

  Если валюта присутствует в списке, последнее поле можете оставить пустым.
  Для изменения существующего значения введите новое.
"""
print(msg)

print_list(list_currency)

# ввод пары
pair_name = input('\n 1) ').strip().upper() or bad_text

if isvalid_pair(pair_name) and pair_name != bad_text:
    val = pair_name.split('/')

    user_info['pair_name']    = pair_name
    user_info['currency']     = val[0]
    user_info['use_currency'] = val[1]

    if user_info['currency'] not in list_currency:
        list_currency[user_info['currency']] = 0
else:
    raise TraderBotException('Формат введенной пары не корректен')
# конец ввода пары

# ввод баланса
balance = int(input(' 2) ') or bad_num)

user_info['status'] = detect_status(balance)

if balance != bad_num:
    user_info['balance'] = balance
else:
    raise TraderBotException('Баланс должен быть больше ' + bad_num)
# конец ввода баланса

# ввод действия
action = input(' 3) ').strip().lower() or bad_text

if action == 'sell' or action == 'buy' and action != bad_text:
    user_info['action'] = action
else:
    raise TraderBotException('Тип проиводимой операции не корректен ' + action)
# конец ввода действия

# ввод текущей цены
current_price = float(input(' 4) ') or bad_num)

if current_price != bad_num:
    user_info['current_price'] = current_price
else:
    raise TraderBotException('Цена должна быть больше ' + bad_num)
# конец ввода текущей цены

# ввод оличества криптовалюты если ее нет в списке просто нажать enter
min_order_size = int(input(' 5) ') or bad_num)

if min_order_size != bad_num:
    list_currency[user_info['currency']] = min_order_size
    user_info['order_size']              = min_order_size
else:
    min_order_size          = list_currency[user_info['currency']]
    user_info['order_size'] = min_order_size
# конец ввода оличества криптовалюты

# вывод информации
msg = """
 Валютная пара: {}
 Баланс:        {}
 Статус:        {}
 Тип операции:  {}
 Биржевая цена: {} для покупки {}
 Размер ордера: {}
""".format(
    user_info['pair_name'],
    user_info['balance'],
    user_info['status'],
    user_info['action'],
    user_info['current_price'], user_info['currency'],
    user_info['order_size']
)
print(msg)

if user_info['action'] == 'buy':
    min_price = float(input(' Введите нижнюю граница цены '))
    calculate_buy(user_info, min_price)

if user_info['action'] == 'sell':
    max_price = float(input(' Введите верхнюю граница цены '))
    calculate_sell(user_info, max_price)


for key in user_info:
    print('', key, ':', user_info[key])
print_list(list_currency)