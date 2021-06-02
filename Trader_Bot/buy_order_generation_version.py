# Промежуточная задача:
# необходимо сгенерировать 100 минимальных ордеров на покупку (BUY-ордера) на отрезке цены от 0.00 RUB  до 1.00 RUB
# причём надо учесть торговую комиссию, которую берёт биржа в размере x % за каждую сделку.
# размер минимального ордера и комиссию вводит пользователь .
# Также после генерации ордеров вывести информации
# сколько fiat необходимо пользователю потратить, и сколько он купит crypto

# имеющиеся данные:
# pair_name : crypto/feat
# currency : crypto
# use_currency : feat
# action : BUY
# minprice: 0.00 feat
# maxprice: 1.00 feat
# orders: 100
# min_deal : n crypto - вводит пользователь
# comission : х % -  вводит пользователь

# в результате пользователь получает : (например вводим данные: min_deal = n = 10 crypto ; comission = x = 10%)

# 1) BUY   0.01 feat    11 crypto   total: 0.01 * 11 feat
# 2) BUY   0.02 feat    11 crypto   total: 0.02 * 11 feat
# 3) BUY   0.03 feat    11 crypto   total: 0.03 * 11 feat
# ...
# 99) BUY   0.99 feat    11 crypto   total: 0.99 * 11 feat
# 100) BUY   1.00 feat    11 crypto   total: 1.00 * 11 feat
# На генерацию 100 минимальных ордеров вам понадобится: ____ feat.
# Если все 100 ордеров отторгуются вы купите ____ crypto
minprice = 0.00
maxprice = 1.00
orders = 100
min_deal = int(input('Введите минимально возможное количество crypto, которое можно купить в 1 ордере: '))
comission = float(input('Введите % тороговой комиссии, которую берёт биржа: '))
min_deal = min_deal + min_deal * comission / 100
tradecomission = comission * 10 / 100
print('\nМинимальная сделка составит: BUY {} crypto минус торговая комиссия {} % \n'
      'Генерируется 100 ордеров на участке (0.00 - 1.00) feat'.format(min_deal, tradecomission))
count = 0
# вычисляем шаг с которым должны быть расставлены ордера
steptrade = (maxprice - minprice) / orders
print('Шаг с которым будут выставленны {} ордеров будет {} feat\n...\n'.format(orders, steptrade))

while orders > 0:
      totalsumm = min_deal * (minprice + steptrade)
      print('{} BUYордер   Цена: {} feat    минимальный ордер: {} crypto     сумма покупки: {}  feat'.format(count + 1, minprice + steptrade, min_deal, totalsumm ))
      count = count + 1
      minprice = minprice + steptrade
      orders = orders - 1
     #  alltotalsumm =
# print('\nчтобы выставить все ордера вам понадобится {} feat'.format(alltotalsumm))
