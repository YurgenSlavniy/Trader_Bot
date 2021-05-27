from re import match
"""
* необходимо обеспечить проверку вводимых данных

Если использовать программу для себя, то известно какие данные нужно ввести.
	если вместо RUB/EXM будет введено [rub/exm], [123/456], [100]
	также пара добавляется в список pirs, а что если она вобще некоректна
	даже если ее формат с виду коректен BLA/MUDOFON
	Например: Минимальная и максимальная длина len(pains[i]) + регистер символов

* необходимо улучшить выводимые сообщения, чтобы было коротко и понятно
"""

# start ----------------- ЗДЕСЬ БЫЛИ ИЗМЕНЕНИЯ ------------------------ #

############################## LIBRARY ##################################
# function для проверки корректности пары
def isvalid_pair(pair):
	# если длина корректна length True
	length = len(pair) > 6 and len(pair) < 20
	# если формат корректен format_correctly True
	format_correctly = match(r'[A-Z/]{6,20}', pair)

	if length and format_correctly:
		return True
	else:
		return False
############################# END LIBRARY ###############################

# Список пар
pairs = [
	'EXM/RUB',  'SMART/RUB', 'XRP/RUB',
	'ALGO/RUB', 'BTT/RUB',   'DAI/RUB',
	'ONG/RUB',  'ONT/RUB',   'TRX/RUB',
    'USDT/RUB', 'XLM/RUB',   'LSK/RUB',
]

# Иоформация о пользователе
user_info = {
	'pair_name':    '',   # пара
	'buy_currency': '',   # что покупаем
	'use_currency': '',   # за что покупаем
	'status':       '',   # статус пользователя
	'action':       '',   # действие sell/buy
	'balance':       0,   # общий баланс
	'current_price': 0.0, # текущая цена вылюты
} 

# Формируем сообщение
message = """
 Привет, Я финансовый помошник. 
 Kоторый поможет сгенерировать ордера для биржи криптовалют.

 Для генерации ордеров необходимо будет ввести запрашиваемые
 программой данные.

 ЗАПРОС: 1
 Введите название торговой пары. 
"""
# Выводим сообщение
print(message)

# Вывод имеющихся пар
for i in range( len(pairs) ):
	print(" {pair:<10s} ".format(pair=pairs[i]), end='')	
	if (i + 1) % 4 == 0:
		print()

"""
+ Ввод названя пары, вводить можно только такой формат EXM/RUB и exm/rub
+ удалить пробелы strip
+ переводим в вегхний регистер upper
"""
user_info['pair_name'] = input('\n\n Пара: ').strip().upper()

# Если пара валидная в ней нет некорректных символов
if isvalid_pair(user_info['pair_name']):
	# Если пары нет в списке pairs, то добавляем
	if user_info['pair_name'] not in pairs:
		pairs.append(user_info['pair_name'])
else:
	raise Exception('Введенная пара не корректна')

# Разбиваем пару 
break_pair = user_info['pair_name'].split('/')

user_info['buy_currency'] = break_pair[0] # вылюта которую покупаем 
user_info['use_currency'] = break_pair[1] # вылюта которую используем для покупки

# end ----------------- ДАЛЬШЕ НЕТ ИЗМЕНЕНИЙ ------------------------ #
print(pairs)
print(user_info)
input('---------------------------------------------------------------')
# Формируем сообщение
message = """
 ЗАПРОС: 2
 Сколько вы готовы инвестировать в эту валютную пару в рублях?
"""
print(message)

# Ввод суммы
user_info['balance'] = int(input(' Сумма: '))

# Определяем статус пользователя
if user_info['balance'] < 11111:
	user_info['status'] = 'babyplay'

elif user_info['balance'] >= 11111 and user_info['balance'] < 55555:
	user_info['status'] = 'junior'

elif user_info['balance'] >= 55555 and user_info['balance'] < 111111:
	user_info['status'] = 'Segnior'

elif user_info['balance'] >= 111111 and user_info['balance'] < 1111111:
	user_info['status'] = 'VipSegnior'

elif user_info['balance'] >= 1111111:
	user_info['status'] = 'TraderKing'

# Формируем сообщение
message = """
 Ваш баланс: {balance} рублей.

 ЗАПРОС: 3
 Тип операции: Покупка введите BUY  или buy
               Продажа введите SELL или sell
""".format(balance=user_info['balance'])

# Вывод баланса и предложение на дальнейшие действия
print(message)

# Ввод действия buy или sell + удалить пробелы
user_info['action'] = input(' Действие: ').strip()

print('\n ЗАПРОС: 4\n Введите биржевую цену ', end='')

# Ввод текущей цены buy или sell
if user_info['action'].lower() == 'buy':
	user_info['current_price'] = float(input('"ПОКУПКИ" на данный момент: '))

if user_info['action'].lower() == 'sell':
	user_info['current_price'] = float(input('"ПРОДАЖИ" на данный момен: '))

# Формируем сообщение
message = """
 Cобранные данные:
  Вы хотите торговать в валютной паре - {pair}
  Вы готовы инвестировать в неё       - {balance} рублей
  Ваш статус                          - {status}
  Тип производимой операции           - {action} по цене "{current_price}"

 Подождите...
""".format(
		pair=user_info['pair_name'],
		status=user_info['status'], 
		balance=user_info['balance'],
		action=user_info['action'],
		current_price=user_info['current_price']
	)

# Вывод введенной информации
print(message)