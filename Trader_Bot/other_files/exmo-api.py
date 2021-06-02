import requests as request

"""
	Можно получить различную информацию c EXMO
	Запустить в терминале установки библиотеки requests 
		так pip install requirements.txt
		или pip3 install requirements.txt
"""

# 
# Список сделок по валютной паре
"""
	Example
{ 
	'trade_id': 275844174, 
	'date': 1622299713, 
	'type': 'buy', 
	'quantity': '0.044', 
	'price': '2563937.86', 
	'amount': '112813.26584'
}

"""
# Например: получить сделок по валютной паре BTC_RUB
result = request.post('https://api.exmo.com/v1.1/trades', data={'pair': 'BTC_RUB'})
if result.status_code == 200:
	for pair in result.json():
		print('Список сделок по валютной паре:\n', pair)
		for elem in result.json()[pair]:
			print(f"type:{elem['type']},	quantity:{elem['quantity']},\
	price:{elem['price']},	amount:{elem['amount']}"

		)
# Также можно получить: Статистика цен и объемов торгов по валютным парам
# {
#   "BTC_USD": {
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

# Также можно получить (какая-то): Книга текущих заявок по валютной паре

# {
#   "BTC_USD": {
#     "ask_quantity": "3",
#     "ask_amount": "500",
#     "ask_top": "100",
#     "bid_quantity": "1",
#     "bid_amount": "99",
#     "bid_top": "99",
#     "ask": [ [
#         100,
#         1,
#         100
#       ],
#       [
#         200,
#         2,
#         400
#       ]
#     ],
#     "bid": [
#       [
#         99,
#         1,
#         99
#       ]
#     ]
#   }
# }

# Настройки валютных пар

# {
#   "EXM_ETH": {
#     "min_quantity": "1",
#     "max_quantity": "1000",
#     "min_price": "1",
#     "max_price": "1000",
#     "max_amount": "1000",
#     "min_amount": "1",
#     "price_precision": 8,
#     "commission_taker_percent": "0.2",
#     "commission_maker_percent": "0.2"
#   },
#   "BTC_USD": {
#     "min_quantity": "0.001",
#     "max_quantity": "100",
#     "min_price": "1",
#     "max_price": "10000",
#     "max_amount": "30000",
#     "min_amount": "1",
#     "price_precision": 2,
#     "commission_taker_percent": "0.2",
#     "commission_maker_percent": "0.2"
#   }
# }

# Список валют

# [
#   "USD",
#   "EUR",
#   "RUB",
#   "BTC",
#   "DOGE",
#   "LTC"
# ]

# Расширенный список валют

# [
#   {
#     "name": "USD",
#     "description": "US Dollar"
#   },
#   {
#     "name": "UAH",
#     "description": "Ukrainian hryvnia"
#   }
# ]

# Расчет суммы покупки определенного количества валюты для конкретной валютной пары

# {
#   "quantity": 3,
#   "amount": 5,
#   "avg_price": 3.66666666
# }

# Какуюто историю

# {
#   "candles": [
#     {
#       "t": 1585557000000,
#       "o": 6590.6164,
#       "c": 6602.3624,
#       "h": 6618.78965693,
#       "l": 6579.054,
#       "v": 6.932754980000013
#     }
#   ]
# }


# Crypto providers list
# {
# "BTC": [
#     {
#       "type": "deposit", //provider method type, withdrawal or deposit
#       "name": "BTC", //provider name
#       "currency_name": "BTC", //currency name
#       "min": "0", //min amount per operation
#       "max": "0", //max amount per operation
#       "enabled": true, //provider status
#       "comment": "", //comment for provider
#       "commission_desc": "", //description of commission
#       "currency_confirmations": 0 //the number of required confirmations for the operation
#     },
#     {
#       "type": "withdraw",
#       "name": "BTC",
#       "currency_name": "BTC",
#       "min": "0.01",
#       "max": "350.001",
#       "enabled": true,
#       "comment": "",
#       "commission_desc": "",
#       "currency_confirmations": 3
#     }
# ],
#   "LTC": [
#     {
#       "type": "deposit",
#       "name": "LTC",
#       "currency_name": "LTC",
#       "min": "0",
#       "max": "0",
#       "enabled": true,
#       "comment": "",
#       "commission_desc": "",
#       "currency_confirmations": 0
#     },
#     {
#       "type": "withdraw",
#       "name": "LTC",
#       "currency_name": "LTC",
#       "min": "0.5",
#       "max": "1050",
#       "enabled": true,
#       "comment": "",
#       "commission_desc": null,
#       "currency_confirmations": 50
#     }
# ]
# }