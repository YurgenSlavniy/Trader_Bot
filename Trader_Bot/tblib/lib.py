from re import match

class TraderBotException(Exception):
    pass

def isvalid_pair(pair):
    format_correctly = match(r'[A-Z/]{6,20}', pair)

    if format_correctly:
        return True
    else:
        return False

def print_list(list_curr):
    count = 0
    print(' Список вылют:')
    for key in list_curr:
        print(" {:<2s}:{} ".format(key, list_curr[key]), end='')
        count += 1
        if count % 4 == 0:
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

def calculate_buy(user_info, min_price):
    min_order_size = user_info['order_size']
    current_price  = user_info['current_price']
    balance        = user_info['balance']

    fixed_order_price = current_price * min_order_size
    total_orders      = balance / fixed_order_price

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

def calculate_sell(user_info, max_price):
    min_order_size = user_info['order_size']
    current_price  = user_info['current_price']
    balance        = user_info['balance']
    
    total_real_deals  = balance // (current_price * min_order_size)
    total_currency    = balance / current_price
    total_sell_orders = total_currency / min_order_size

    step = (max_price - current_price) / total_sell_orders
    
    count = 0
    while True:
        count += 1

        if total_sell_orders <= 0: break
        
        message = '{:<5}{} Количество валюты: {:<10f} {} Продаём за: {:<10f} {} На сумму: {:<10f} {}'.format(
            count,
            user_info['action'],
            user_info['order_size'],
            user_info['currency'],
            current_price,
            user_info['use_currency'],
            min_order_size * current_price,
            user_info['use_currency']
        )

        print(message)

        current_price += step
        total_sell_orders = int(total_sell_orders) - 1