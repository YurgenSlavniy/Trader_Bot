# Описание.
# Пользователь вводит данные:
# - цену на бирже на даный момент времени ,
# - минимальную цены покупки,
# - максимальную цену продажи,
# шаг с которым будем расставлять ордера
# (также может  данные можно брать с помощью API непосредственно с биржи EXMO.me)
# Программа расставляет минимальные ордера на заданном отрезке цены
# и выводит пользователю итоговую сумму сколько пользователю понадобится денег (рублей)
# чтобы расставить ордера с заданными параметрами. Комиссия в торговой паре учитывается.

# Для простоты мы начнём с одной валютной пары:
# EXM/RUB.
# так как пара конкретная, то и некоторые показатели нам уже точно известны:
pair_name = 'EXM/RUB'
currency = 'EXM'
use_currency = 'RUB'
min_deal = 10    # минимальный ордер 10 EXM
trade_percent = 1   # 1 %   - торговая комиссия за каждую сделку

# приветственное сообщение
print('\nЭта программа произведёт расчёт количества необходимых ДЕНЕЖНЫХ СРЕДСТВ\n'
      'для расстановки минимальных торговых ордеров с заданным шагом.\n'
      'Расчёт будет производиться для торговой пары {}\n'.format(pair_name))

# здесь можно было бы подключиться по API к бирже, отпаривть запрос и вывести пользователю данные по валютной бирже .
# ты добавлял файл даже какой то exmo-api.py. Это оттуда: Но как подключиться
# Я НЕ ЗНАЮ КАК ЭТО РАБОТАЕТ
# Также можно получить: Статистика цен и объемов торгов по валютным парам
# {
#   "EXM_RUB": {
#     "buy_price": "589.06",
#     "sell_price": "592",
#     "last_trade": "591.221",
#     "high": "602.082",
#     "low": "584.51011695",
#     "avg": "591.14698808",
#     "vol": "167.59763535",
#     "vol_curr": "99095.17162071",
#     "updated": 1470250973
#   }
# }
print('Текущие данные с биржи: цена на бирже = ... и другие данные\n') # формируем сообщение вывода информации с биржи

# пошли запросы , чтобы пользователь вводил данные
print('Введите запрашиваемую информацию, для генерации и расчёта:')
price = input('Запрос 1: Введите цену на бирже: ')
price = float(price)
min_price = input('Запрос 2: Введите минимальную цену за которую готовы купить EXM: ')
min_price = float(min_price) # сперва вводим, потом меняю type даннных.
# При вводе принимает строкой любой ввод и не ругается, когда вводим целое число без точки
max_price = input('Запрос 3: Введите максимальную цену за которую готовы продать EXM: ')
max_price = float(max_price)
trade_step = input('Запрос 4: Введите шаг с которым нужно расставить ордера: ')
trade_step = float(trade_step)

# После ввода данных выводим сообщение с некоторыми расчётами пользователю, для подтверждения готовности генерации.
print('\nПоехали!\n')
# для генерации BUY ордеров:
buy_value = price - min_price # вычислили отрезок на котором расставаляем BUY ордера . [min_price, price]
buy_orders = int(buy_value / trade_step) # вычисляем сколько ордеров с указанным шагом мы можем выставить на BUY отрезке цены
# вычисляем какая сумма денег понадобится на расстановку всех BUY ордеров с учётом торговой комиссии
buy_money = 0
total_buy_money = 0
order_price = price # цена первого ордера равна рыночной цене
min_order_value = min_deal + (min_deal * trade_percent / 100)
while order_price >= min_price:
      order_price = order_price - trade_step
      buy_money = min_order_value * order_price
      total_buy_money = total_buy_money + buy_money
      print('BUY  price: {} RUB   количество: {} EXM на сумму: {} {}'.format(order_price, min_order_value, buy_money, use_currency ))

print('\nБудет выставлено {} BUY ордеров\nДля этого вам понадобится сумма: {} RUB'.format(buy_orders, total_buy_money, ))
print('\nдля продолжения нажмите ентер')
enter = input('')
# для генерации SELL ордеров:
sell_value = max_price - price # вычислили отрезок на котором расставаляем SELL ордера
sell_orders = int(sell_value / trade_step)  # вычисляем сколько ордеров с указанным шагом мы можем выставить на SELL отрезке цены
# вычисляем какая сумма денег понадобится на расстановку всех SELL ордеров с учётом торговой комиссии
sell_money = 0
total_sell_money = 0
sell_order_price = price # цена первого ордера равна рыночной цене
min_order_value = min_deal + (min_deal * trade_percent / 100)
while sell_order_price <= max_price:
      sell_order_price = sell_order_price + trade_step
      sell_money = min_order_value * sell_order_price
      total_sell_money = total_sell_money + sell_money
      print('BUY  price: {} RUB   количество: {} EXM на сумму: {} {}'.format(sell_order_price, min_order_value, sell_money, use_currency ))
print('\nБудет выставлено {} sell ордеров\nДля этого вам понадобится сумма: {} RUB\n'.format(sell_orders, total_sell_money))
total_money = total_sell_money + total_buy_money
print('Общая сумма которая необходима: {} {}'.format(total_money, use_currency))

# работает не совсем корректно,и это нужно будет поправить.
# дальнейшие задачи по этому коду: вывод вместо динныц дробных частей 2 знака после запятой.
# доработать алгоритм расстановке, последний ордер отрицательного значения в buy растановке при тестировании
# в целом всё отрабатывает неплохо в этом модуле
