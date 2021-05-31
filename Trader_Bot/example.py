

pair_name     = 'EXM/RUB'
currency      = 'EXM'
use_currency  = 'RUB'
status        = 'babyplay'
action        = 'buy'
balance       = 456
current_price = 0.69


 # действия без длинных описаний...
 # минимально возможное количество 'EXM' которое мы можем купить в одном ордере.

minbuyorder = 10.00 # Данные вводятся пользователем либо хронятся в настройках торговой пары, если она уже есть.
print('Минимальный ордер покупки составляет: ', minbuyorder, ' EXM \n')

 # расчитаем количество ордеров, которые можно сгенерировать, исходя из имеющихся данных.

fixorderprice = current_price * minbuyorder
ordersvalue = int(balance / fixorderprice)  # 1234/(1 * 10) = 123.4

 # вводим нижнюю границу цены. это последний ордер на покупку.
minprice = 0.0099
 # берём отрезок цены от minprice до current_price (в нашем случае от 0.0099 до 1.00)
 # и расчитываем интервал - шаг между выставляемыми ордерами
pricestep = (current_price - minprice) / ordersvalue


print(
    'На имеющуюся у Вас сумму: ', balance, 'RUB\n',
    'Вы можете выставить ', ordersvalue, ' ордеров на покупку\n',
    'Ордер будет выставлен на фиксированную сумму: ', fixorderprice, ' RUB\n',
    'Ордера будут выставлены на отрезке цены:\n'
    'нижний предел (минимальная цена): ', minprice, ' RUB за 1 EXM \n',
    'верхний предел (рыночная цена на данный момент): ', current_price, ' RUB за 1 EXM \n'
     )



# Выставляется первый ордер результат выводится пользователю:
print('1) BUY   цена: ', current_price, ' ', use_currency , 'сумма ордера: ', fixorderprice, ' ', use_currency, 'количество покупаемой валюты: ', fixorderprice / current_price, ' ', currency )
# После выставления ордера наш баланс уменьшается на fixorderprice
balance = balance - fixorderprice
# Выставляем второй ордер:
current_price = current_price - pricestep
print('2) BUY   цена: ', current_price,  ' ', use_currency , 'сумма ордера: ', fixorderprice, ' ', use_currency, 'количество покупаемой валюты: ', fixorderprice / current_price, ' ', currency )
# После выставления ордера наш баланс уменьшается на fixorderprice
balance = balance - fixorderprice
# Выставляем третий ордер:
current_price = current_price - pricestep
print('3) BUY   цена: ', current_price,  ' ', use_currency , 'сумма ордера: ', fixorderprice, ' ', use_currency, 'количество покупаемой валюты: ', fixorderprice / current_price, ' ', currency )
# Выставляем четвёртый ордер:
current_price = current_price - pricestep
print('4) BUY   цена: ', current_price,  ' ', use_currency , 'сумма ордера: ', fixorderprice, ' ', use_currency, 'количество покупаемой валюты: ', fixorderprice / current_price, ' ', currency )
# Выставляем слдующий ордер:
current_price = current_price - pricestep
print('5) BUY   цена: ', current_price,  ' ', use_currency , 'сумма ордера: ', fixorderprice, ' ', use_currency, 'количество покупаемой валюты: ', fixorderprice / current_price, ' ', currency )
print(...)
# И т.д пока у нас не закончится баланс balance = 0 вышли из цикла - ордера расставлены!

# когда выводим пользователю получаем :
# *) BUY   цена:  0.9919504065040651  RUB, сумма ордера:  10.0  RUB, количество покупаемой валюты:  10.081149152650728  EXM
# цена:  0.9919504065040651  , количество покупаемой валюты:  10.081149152650728  EXM можно округлять до 4 знаков после запятой...

# я тестировал работу с другими данными и забыл, что в папке репозитория работаю.
# и пока не создам коммит, не могу переключиться на другую ветку в гит кракене
# немного изменил вывод с использованием переменных currency, use_currency