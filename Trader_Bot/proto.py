"""
* необходимо юбеспечить проверку вводимых данных
* необходимо улучшить выводимые сообщения, чтобы было коротко и понятно
* думаю все это для прототипа сгодится
* думаю здесь должно быть две программы Клиент и Сервер
* думаю необходимы реальные данные, это API - Биржи
* думаю еще много чего нужно...
"""
# Список пар
pairs = [
	'RUB/EXM', 'BTC/SMART', 'ETH/CRON',
	'RUB/EXM', 'BTC/SMART', 'ETH/CRON',
	'RUB/EXM', 'BTC/SMART', 'ETH/CRON',
]

# Иоформация о пользователе
user_info = {} 

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

# Ввод названя пары + удалить пробелы
user_info['pair_name'] = input('\n\n Пара: ').strip()

# Если пары нет в списке pairs, то добавляем
if user_info['pair_name'] not in pairs:
	pairs.append(user_info['pair_name'])

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