from re import match
"""
* подумать о вводимых данных дополнительно
* необходимо улучшить выводимые сообщения, чтобы было коротко и понятно
* необходимо вычислить повторяющиеся участки кода
* необходимо создать библиотеку в отдельном файле
"""

############################## LIBRARY ##################################
# function проверка корректности пары
def isvalid_pair(pair):
	# если длина корректна length True
	length = len(pair) > 6 and len(pair) < 20
	# если формат корректен format_correctly True
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

""" 
Вывод имеющихся пар
pair:<10s означает выровнять EXM/RUB : по < правому краю с шириной поля 10 символов
"""
for i in range( len(pairs) ):
	print(" {pair:<10s} ".format(pair=pairs[i]), end='')	
	if (i + 1) % 4 == 0:
		print()

"""
+ Ввод названия пары, вводить можно только такой формат EXM/RUB и exm/rub
+ удалить пробелы strip
+ переводим в вегхний регистер upper
+ если пользователь нажал интер не вводя ничего, присваиваем FAIL/IN' неудачный ввод
"""
user_info['pair_name'] = input('\n\n Пара: ').strip().upper() or 'fail/in'

# Если пара валидная в ней нет некорректных символов
if isvalid_pair(user_info['pair_name']) and user_info['pair_name'] != 'fail/in':
	# Если пары нет в списке pairs, то добавляем
	if user_info['pair_name'] not in pairs:
		pairs.append(user_info['pair_name'])
else:
	raise Exception('Введенная пара не корректна')

# Разбиваем пару 
break_pair = user_info['pair_name'].split('/')

user_info['buy_currency'] = break_pair[0] # вылюта которую покупаем 
user_info['use_currency'] = break_pair[1] # вылюта которую используем для покупки


# Формируем сообщение
message = """
 ЗАПРОС: 2
 Сколько вы готовы инвестировать в эту валютную пару в {currency}?
""".format(currency=user_info['use_currency'])

print(message)

# Ввод суммы
user_info['balance'] = int(input(' Сумма: ') or 0)

# Если баланс равен нулю
if user_info['balance'] == 0:
	raise Exception('Сумма должна быть больше ' + str(user_info['balance']))

# Определяем статус пользователя
user_info['status'] = detect_status(user_info['balance'])

""" 
+ Формируем сообщение
+ в тексте будет найден шаблон {balance}
+ balance=user_info['balance'] будет подставленно значение по имени аргумента
"""
message = """
 Ваш баланс: {balance} {currency}.

 ЗАПРОС: 3
 Тип операции: Покупка введите BUY  или buy
               Продажа введите SELL или sell
""".format(
	balance=user_info['balance'],
	currency=user_info['use_currency']
	)

# Вывод баланса и предложение на дальнейшие действия
print(message)

# Ввод действия buy или sell + удалить пробелы
action = input(' Действие: ').strip().lower() or 'fail/in'

# если выбрана корректная опрерация
if action == 'sell' or action == 'buy' and action != 'fail/in':
	user_info['action'] = action
else:
	raise Exception('Действие не корректно ' + action)

user_info['action'] = action

print('\n ЗАПРОС: 4\n Введите биржевую цену ', end='')

# Ввод текущей цены buy или sell
if user_info['action'] == 'buy':
	current_price = float(input('"ПОКУПКИ" на данный момент: ') or 0.0)

if user_info['action'] == 'sell':
	current_price = float(input('"ПРОДАЖИ" на данный момен: ') or 0.0)


if current_price == 0:
	raise Exception('Цена должна быть больше ' + str(current_price))

user_info['current_price'] = current_price

# Формируем сообщение
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

# Вывод введенной информации
print(message)

for el in user_info:
	print(el, ':', user_info[el])

# Кода становится слишком много
