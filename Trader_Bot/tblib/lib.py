from re import match

class TraderBotException(Exception):
    pass

def isvalid_pair(pair):
    format_correctly = match(r'[A-Z/]{6,20}', pair)

    if format_correctly:
        return True
    else:
        return False

def print_currency_list(pairs, size_line):
    print(' Список вылют:')
    size_line += 1
    sep = 0
    for i in range(len(pairs)):
        sep += 1
        if sep != size_line:
            print(' {:<10} '.format(pairs[i]), end='')
        if sep == size_line:
            print()
            sep = 0

def set_status(balance):
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
    # цена одного ордера
    user_info['order_price'] = user_info['current_price'] * user_info['order_size']
    # колличество ордеров
    # total_orders = user_info['balance'] / user_info['order_price']
    total_orders = user_info['ratio_price']['buy'] / user_info['order_price']
    user_info['total_orders'] = int(total_orders)

    step = (user_info['current_price'] - user_info['min_price']) / total_orders
    current_price = user_info['current_price']

    count = 0
    price = 0
    real_price = 0
    while int(total_orders) != 0:
        count += 1
        # колличество вылюты
        totat_currency = user_info['order_price'] / current_price
        # комиссия
        comission = user_info['order_size'] * user_info['comission'] / 100
        # стоимость одного ордера + комиссия
        user_info['real_order_price'] = user_info['order_price'] + comission

        real_price += user_info['real_order_price']
        # итоговая сумм с учетом комиссии
        user_info['real_price'] = real_price
        # итоговая сумм без комиссии
        price += user_info['order_price']
        user_info['price'] = price

        message = ' {:<4}BUY цена: {:<10f} {} Сумма ордера + %: {:<10f} {} Количество криптовалюты: {:<10f} {}'.format(
            count,
            current_price,
            user_info['use_currency'],
            user_info['real_order_price'],
            user_info['use_currency'],
            totat_currency,
            user_info['currency']

        )

        print(message)
        
        current_price -= step
        total_orders  -= 1

def calculate_sell(user_info):
    # колличество валюты
    # total_currency = user_info['balance'] / user_info['current_price']
    total_currency = user_info['ratio_price']['sell'] / user_info['current_price']
    user_info['total_currency'] = total_currency

    # количество ордеров
    total_orders = total_currency / user_info['order_size']
    user_info['total_orders'] = int(total_orders)

    step = (user_info['max_price'] - user_info['current_price']) / total_orders
    current_price = user_info['current_price']

    # цена за все ордера
    user_info['price'] = total_currency * current_price
    
    count = 0
    profit = 0
    while int(total_orders) != 0:
        count += 1

        message = ' {:<4}SELL Количество валюты: {:<10f} {} Продаём за: {:<10f} {} На сумму: {:<10f} {}'.format(
            count,
            user_info['order_size'],
            user_info['currency'],
            current_price,
            user_info['use_currency'],
            user_info['order_size'] * current_price,
            user_info['use_currency']
        )

        print(message)

        current_price += step
        profit += (user_info['order_size'] * current_price)
        total_orders -= 1
    
    user_info['profit'] = [profit, profit - user_info['price']]

def print_buy_info(user_info):
    message = '\n Цена ордера : {} 1/{}'.format(
        user_info['pair_name'],
        user_info['order_price'],
    )
    print(message)
    message = ' Цена ордеров: {} {}/{}'.format(
        user_info['pair_name'],
        user_info['total_orders'],
        user_info['price'],
    )
    print(message)
    message = ' Цена ордера : {} 1/{} + {}% комиссия'.format(
        user_info['pair_name'],
        user_info['real_order_price'],
        user_info['comission'],
    )
    print(message)
    message = ' Цена ордеров: {} {}/{} + {}% комиссия'.format(
        user_info['pair_name'],
        user_info['total_orders'],
        user_info['real_price'],
        user_info['comission'],
    )
    print(message)
    print(' Баланс:', user_info['balance'], user_info['use_currency'])
    print(' Цена:', user_info['real_price'], user_info['use_currency'])

def print_sell_info(user_info):
    message = '\n По рыночной цене {} {} Куплено {} {} На сумму {} {}'.format(
        user_info['current_price'],
        user_info['use_currency'],
        user_info['total_currency'],
        user_info['currency'],
        user_info['price'],
        user_info['use_currency']
    )
    print(message)
    message = ' Количество ордеров {} на сумму {} {}'.format(
        user_info['total_orders'],
        user_info['profit'][0],
        user_info['use_currency'],
    )
    print(message)
    message = ' Профицит для заработка составил: {} {}'.format(
        user_info['profit'][1],
        user_info['use_currency'],
    )
    print(message)

def print_info(user_info):
    msg = """
 Валютная пара: {}
 Баланс:        {}
 Статус:        {}
 Тип операции:  {}
 Биржевая цена: {} для покупки {}
 Размер ордера: {}
 Комиссия       {}
    """.format(
    user_info['pair_name'],
    user_info['balance'],
    user_info['status'],
    user_info['action'],
    user_info['current_price'], user_info['currency'],
    user_info['order_size'],
    user_info['comission'],
)
    print(msg)