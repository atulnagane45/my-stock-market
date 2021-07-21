# this is the tick data for 2 stocks get all the values sepetared

import datetime
from pprint import pprint
data = [{'tradable': True, 'mode': 'full', 'instrument_token': 121345, 'last_price': 21884.85, 'last_quantity': 1, 'average_price': 21847.28, 'volume': 458, 'buy_quantity': 1, 'sell_quantity': 0, 'ohlc': {'open': 22054.1, 'high': 22054.1, 'low': 21730.0, 'close': 21915.85}, 'change': -0.14145013768573886, 'last_trade_time': datetime.datetime(2019, 7, 19, 15, 29, 54), 'oi': 0, 'oi_day_high': 0, 'oi_day_low': 0, 'timestamp': datetime.datetime(2019, 7, 19, 17, 6, 26), 'depth': {'buy': [{'quantity': 1, 'price': 21884.85, 'orders': 1}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}], 'sell': [{'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}]}}, {'tradable': True, 'mode': 'full', 'instrument_token': 1793, 'last_price': 1638.7, 'last_quantity': 9, 'average_price': 1659.16, 'volume': 131464, 'buy_quantity': 566, 'sell_quantity': 0, 'ohlc': {'open': 9999999695.0, 'high': 1695.0, 'low': 1600.0, 'close': 1679.2}, 'change': -2.4118627918056217, 'last_trade_time': datetime.datetime(2019, 7, 19, 15, 29, 51), 'oi': 0, 'oi_day_high': 0, 'oi_day_low': 0, 'timestamp': datetime.datetime(2019, 7, 19, 17, 6, 26), 'depth': {'buy': [{'quantity': 566, 'price': 1638.7, 'orders': 6}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}], 'sell': [{'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}]}}, {'tradable': True, 'mode': 'full', 'instrument_token': 3038209, 'last_price': 96.9, 'last_quantity': 40, 'average_price': 98.69, 'volume': 64374, 'buy_quantity': 68, 'sell_quantity': 0, 'ohlc': {'open': 102.0, 'high': 102.45, 'low': 95.85, 'close': 100.0}, 'change': -3.0999999999999943, 'last_trade_time': datetime.datetime(2019, 7, 19, 15, 48, 39), 'oi': 0, 'oi_day_high': 0, 'oi_day_low': 0, 'timestamp': datetime.datetime(2019, 7, 19, 17, 6, 26), 'depth': {'buy': [{'quantity': 68, 'price': 96.9, 'orders': 2}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}], 'sell': [{'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 4.99999, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}]}}]

exampke = {"mago": 40, "apple": 50}
print(exampke['mago'])


# pprint.pprint(data[2])


pprint(data[2]['depth']['sell'][2]['price'])

# which data struct is it.. check forst bracket
# what are the keys/index
# in which key does my value come


# 1. - 0.14145013768573886
# 2.  9999999695.0
# 3. 39 ... compny 3 .. datetime.. second
# 4. 999999999999999999999999999999

# 40
# {'average_price': 98.69,
#  'buy_quantity': 68,
#  'change': -3.0999999999999943,
#  'depth': {'buy': [{'orders': 2, 'price': 96.9, 'quantity': 68},
#                    {'orders': 0, 'price': 0.0, 'quantity': 0},
#                    {'orders': 0, 'price': 0.0, 'quantity': 0},
#                    {'orders': 0, 'price': 0.0, 'quantity': 0},
#                    {'orders': 0, 'price': 0.0, 'quantity': 0}],
#            'sell': [{'orders': 0, 'price': 0.0, 'quantity': 0},
#                     {'orders': 0, 'price': 0.0, 'quantity': 0},
#                     {'orders': 0, 'price': 5.0, 'quantity': 0},
#                     {'orders': 0, 'price': 0.0, 'quantity': 0},
#                     {'orders': 0, 'price': 0.0, 'quantity': 0}]},
#  'instrument_token': 3038209,
#  'last_price': 96.9,
#  'last_quantity': 40,
#  'last_trade_time': datetime.datetime(2019, 7, 19, 15, 48, 39),
#  'mode': 'full',
#  'ohlc': {'close': 100.0, 'high': 102.45, 'low': 95.85, 'open': 102.0},
#  'oi': 0,
#  'oi_day_high': 0,
#  'oi_day_low': 0,
#  'sell_quantity': 0,
#  'timestamp': datetime.datetime(2019, 7, 19, 17, 6, 26),
#  'tradable': True,
#  }
