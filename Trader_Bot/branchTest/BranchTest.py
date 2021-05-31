from re import match

############################## LIBRARY ##################################
class TraderBotException(Exception):
	pass
# function проверка корректности пары.

def isvalid_pair(pair):

	length = len(pair) > 6 and len(pair) < 20
	format_correctly = match(r'[A-Z/]{6,20}', pair)

	if length and format_correctly:
		return True
	else:
		return False

# futnction установить статус пользователя
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

# funtion распечатать пары
def print_pairs(pairs):
	for i in range( len(pairs) ):
		print(" {pair:<10s} ".format(pair=pairs[i]), end='')
		if (i + 1) % 4 == 0:
			print()
############################# END LIBRARY ###############################

bad_text  = ''
bad_num   = 0

pairs = [
	'EXM/RUB',  'SMART/RUB', 'XRP/RUB',
	'ALGO/RUB', 'BTT/RUB',   'DAI/RUB',
	'ONG/RUB',  'ONT/RUB',   'TRX/RUB',
    'USDT/RUB', 'XLM/RUB',   'LSK/RUB',
]

user_info = {
	'pair_name':     '',
	'currency':      '',
	'use_currency':  '',
	'status':        '',
	'action':        '',
	'balance':        0,
	'current_price':  0,
	'min_deal'     :  0,
	'min_deals':      0,
}

message = """
 Привет, Я финансовый помошник. 
 Kоторый поможет сгенерировать ордера для биржи криптовалют.

 Для генерации ордеров необходимо будет ввести запрашиваемые
 программой данные.

 ЗАПРОС: 1
 Введите название торговой пары. 
"""

print(message)

print_pairs(pairs);

pair_name = input('\n\n Пара: ').strip().upper() or bad_text

if isvalid_pair(pair_name) and pair_name != bad_text:
	if pair_name not in pairs:
		pairs.append(pair_name)
else:
	raise TraderBotException('Введенная пара не корректна')

user_info['pair_name'] = pair_name

break_pair = user_info['pair_name'].split('/')

user_info['currency']      = break_pair[0] # вылюта
user_info['use_currency']  = break_pair[1] # вылюта которую используем для покупки

message = """
 ЗАПРОС: 2
 Сколько вы готовы инвестировать в эту валютную пару в {currency}?
""".format(currency=user_info['use_currency'])

print(message)

user_info['balance'] = int(input(' Сумма: ') or bad_num)

if user_info['balance'] == bad_num:
	raise TraderBotException('Сумма должна быть больше ' + str(user_info['balance']))

user_info['status'] = detect_status(user_info['balance'])

message = """
 Ваш баланс: {balance} {currency}.

 ЗАПРОС: 3
 Тип операции: Покупка введите BUY  или buy
               Продажа введите SELL или sell
""".format(
	balance=user_info['balance'],
	currency=user_info['use_currency']
	)

print(message)

action = input(' Действие: ').strip().lower() or bad_text

if action == 'sell' or action == 'buy' and action != bad_text:
	user_info['action'] = action
else:
	raise TraderBotException('Действие не корректно ' + action)

user_info['action'] = action

print('\n ЗАПРОС: 4\n Введите биржевую цену ', end='')

if user_info['action'] == 'buy':
	current_price = float(input('"ПОКУПКИ" на данный момент: ') or bad_num)

if user_info['action'] == 'sell':
	current_price = float(input('"ПРОДАЖИ" на данный момен: ') or bad_num)

if current_price == bad_num:
	raise TraderBotException('Цена должна быть больше ' + str(current_price))

user_info['current_price'] = current_price

message = """
 Cобранные данные:
  Вы хотите торговать в валютной паре - {pair}
  Вы готовы инвестировать в неё       - {balance} рублей
  Ваш статус                          - {status}

 Подождите...
""".format(
		pair=user_info['pair_name'],
		status=user_info['status'],
		balance=user_info['balance'],
	)

print(message)

print('\n ЗАПРОС: 5\n Минимальная величина сделки \n')

user_info['min_deal'] = float(input(' Размер сделки ') or bad_num)

if user_info['min_deal'] == bad_num:
	raise TraderBotException('Минимальная величина должна быть больше ' + user_info['min_deal'])

user_info['min_deals'] = user_info['balance'] // (user_info['current_price'] * user_info['min_deal'])

print('\n\n Информация для отладки\n')
print(
	' Волютная пара:               {}\n'.format(user_info['pair_name']),
	'Валюта:                      {}\n'.format(user_info['currency']),
	'Валюта для операций:         {}\n'.format(user_info['use_currency']),
	'Статус пользователя:         {}\n'.format(user_info['status']),
	'Действие buy/sell:           {}\n'.format(user_info['action']),
	'Баланс:                      {} {}\n'.format(user_info['balance'], user_info['use_currency']),
	'Текущая цена:                {}\n'.format(user_info['current_price']),
	'Минимальна величина сделки:  {}\n'.format(user_info['min_deal']),
	'Количество возможных сделок: {} ордеров\n'.format(user_info['min_deals']),
)
for el in user_info:
	print(' ' + el, ':', user_info[el])



# ПОПРОБУЮ НАКИДАТЬ ОДИН ИЗ ВАРИАНТОВ ГЕНЕРАЦИИ КОДА СЮДА
print('--- идёт генерация ордеров --- >\n')

# Вариант расстановки SELL сделок:
# сперва мы должны на всю сумму balance купить валюту currency по рыночной цене current_price
sellpairvalue = user_info['balance'] / user_info['current_price']
print(
	'По рыночной цене ', user_info['current_price'], ' ', user_info['use_currency'],
	' покупаем ', sellpairvalue, ' ', user_info['currency'],
	' на общую сумму ', user_info['balance'], ' ', user_info['use_currency']
)
# Теперь нам нужно выставить ордера на продажу.
# зная параметр user_info['min_deal'], расчитаем число ордеров на продажу,
# которое теперь мы можем выставить
sellordersvalue = sellpairvalue // user_info['min_deal']
print('Теперь можно выставить ', sellordersvalue, ' минимальных ордеров на продажу SELL \n')
# теперь нам нужен отрезок цены на котором будут выставлены ордера,
# для этого запросим у пользователя верхний предел цены,
# т.е максимальную цену по которой он выставит последний минимальный ордер на продажу
print('ЗАПРОС: 6')
print('Напоминаем цену покупки: ', user_info['current_price'], ' ', user_info['use_currency'], ' за 1 ', user_info['currency'] )
maxsellorder = float(input('Введите максимальную цену продажи: '))

# теперь есть корридор от user_info['current_price'] до maxsellorder,
# и мы раситываем шаг с которым будут расставлены ордера
stepsell = (maxsellorder - user_info['current_price']) / sellordersvalue
print('Мы расчитали шаг с которым будем расставлять ордера: ', stepsell)
print('В диапазоне цены от ', user_info['current_price'], ' до ',  maxsellorder, ' будет расставлено ', sellordersvalue, ' ордеров.\n' )
print('--- идёт генерация ордеров --- >\n')

# выставляем ордера:
sellprofit = 0
while sellpairvalue > 0:
	print(
		'SELL: количество валюты: ', user_info['min_deal'], ' ', user_info['currency'],
		' продаём за ', user_info['current_price'], ' ', user_info['use_currency'],
		' на сумму ', user_info['min_deal'] * user_info['current_price'], ' ', user_info['use_currency']
	)
	sellpairvalue = sellpairvalue - user_info['min_deal']
	user_info['current_price'] = user_info['current_price'] + stepsell
	sellprofit = sellprofit + (user_info['min_deal'] * user_info['current_price'])
print('сгенерировано ', sellordersvalue, ' ордеров на общую сумму ', sellprofit, ' ', user_info['use_currency'])