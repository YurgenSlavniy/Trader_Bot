print('Я финансовый помошник, который поможет сгенерировать ордера для биржи криптовалют.')
print('Для генерации ордеров необходимо будет ввести запрашиваемые программой данные.')
print('Запрос 1')
tradepeir = input('Введите название торговой пары (например:RUB/EXM, BTC/SMART, ETH/CRON и т.д ): ')
print('Запрос 2')
balance = int(input('Сколько вы готовы инвестировать в эту валютную пару в рублях? введите сумму: '))
print('У вас на счету ',balance ,'рублей. \n выбирите операцию ')
print('Запрос 3')
operation = input('Для покупки криптовалюты напишите: BUY, для продажи напишите: SELL ')
if operation == 'BUY':
    print('Запрос 4')
    buyprice = float(input('введите биржевую цену покупки на данный момент: '))
elif operation == 'SELL':
    print('Запрос 4')
    sellprice = float(input('введите биржевую цену продажи на данный момент: '))
print('собранные данные: \n Вы хотите торговать в валютной паре ', tradepeir, '\n и готовы инвестировать в неё ', balance, ' рублей \n' )
print('... подождите генерируются ордера ...')
print('Для вывода результата нажмите enter')