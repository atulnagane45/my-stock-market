import datetime
import pprint
data = {'tradable': True, 'mode': 'full', 'instrument_token': 325121, 'last_price': 23359.1, 'last_quantity': 1, 'average_price': 0.0, 'volume': 0, 'buy_quantity': 0, 'sell_quantity': 0, 'ohlc': {'open': 23996.9, 'high': 23996.9, 'low': 23140.05, 'close': 23359.1}, 'change': 0.0, 'last_trade_time': datetime.datetime(2019, 4, 9, 15, 29, 53), 'oi': 0, 'oi_day_high': 0, 'oi_day_low': 0, 'timestamp': None, 'depth': {'buy': [{'quantity': 0, 'price': 99.80, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}], 'sell': [{'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}]}}


pprint.pprint(data['depth']['buy'][0]['price'])
