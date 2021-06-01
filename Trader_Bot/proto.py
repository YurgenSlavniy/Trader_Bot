from re import match

class TraderBotException(Exception):
    pass

bad_text = ''
bad_num  = 0

list_currency = {
    'EMX': 10, 'XRP': 20, 'DAI': 30, 'XLM': 40,
    'LSK': 50, 'ONG': 60, 'ONT': 70, 'TRX': 80,
}

user_info = {}
############################# LIBRARY ###################################
def isvalid_pair(pair):
    format_correctly = match(r'[A-Z/]{6,20}', pair)

    if format_correctly:
        return True
    else:
        return False

def print_list(list_curr):
    count = 0
    for key in list_curr:
        print(" {:<2s}:{} ".format(key, list_curr[key]), end='')
        count += 1
        if count % 8 == 0:
            print()

def detect_status(balance):
    status = ''
    if balance < 11111:
        status = 'babyplay'

    elif balance >= 11111 and balance < 55555:
        status = 'junior'

    elif balance >= 55555 and balance < 111111:
        status = 'Segnior'

    elif balance >= 111111 and balance < 1111111:
        status = 'VipSegnior'

    elif balance >= 1111111:
        status = 'TraderKing'
    return status

def trim_tail(num, tail_size):
    nstr = str(num).split('.')
    tail = ''
    for i in range(len(nstr[1])):
        if i < tail_size:
            tail += nstr[1][i]
    return nstr[0] + '.' + tail

def calculate_buy(user_info):
    min_order_size = user_info['order_size']
    current_price  = user_info['current_price']
    balance        = user_info['balance']

    fixed_order_price = current_price * min_order_size
    total_orders      = balance / fixed_order_price

    min_price = float(input(' Введите нижнюю граница цены '))
    step      = (current_price - min_price) / total_orders

    count = 0
    while True:
        count += 1

        if balance < fixed_order_price: break

        user_info['balance'] = balance

        message = '{:<5}{} цена: {:<10f} {} Сумма ордера: {:<10f} {} Количество криптовалюты: {:<10s} {}'.format(
            count,
            user_info['action'].upper(),
            current_price,
            user_info['use_currency'],
            fixed_order_price,
            user_info['use_currency'],
            trim_tail(fixed_order_price / current_price, 4),
            user_info['currency']

        )

        current_price -= step
        balance       -= fixed_order_price
        print(message)

def calculate_sell(user_info):
    pass
############################# END LIBRARY ################################
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

print(' Список вылют:')
print_list(list_currency)

# ввод пары
pair_name = input('\n 1) ').strip().upper() or bad_text

if isvalid_pair(pair_name) and pair_name != bad_text:
    val = pair_name.split('/')

    user_info['pair_name']       = pair_name
    user_info['currency']        = val[0]
    user_info['use_currency']    = val[1]

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
action = input(' 3) ') or bad_text

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
    calculate_buy(user_info)

if user_info['action'] == 'sell':
    calculate_sell(user_info)


for key in user_info:
    print(key, ':', user_info[key])
print_list(list_currency)
