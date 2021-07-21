import datetime
from pprint import pprint

listofstocks = ["3MINDIA", "63MOONS", "AARTIIND", "ABAN", "ABB", "ABFRL", "ACC", "ACE", "ADANIENT", "ADANIPORTS", "ADANIPOWER", "AIAENG", "AJANTPHARM", "AKZOINDIA", "ALBK", "ALKEM", "ALLCARGO", "AMARAJABAT", "AMBUJACEM", "ANANTRAJ", "APOLLOHOSP", "APOLLOTYRE", "ARVIND", "ASAHIINDIA", "ASHOKLEY", "ASIANPAINT", "ASTRAZEN", "ATFL", "ATUL", "AUBANK", "AUROPHARMA", "AUTOAXLES", "AVANTIFEED", "AXISBANK", "BAJAJ-AUTO", "BAJAJELEC", "BAJAJFINSV", "BAJAJHLDNG", "BAJFINANCE", "BALKRISIND", "BALRAMCHIN", "BANCOINDIA", "BANKBARODA", "BANKBEES", "BANKINDIA", "BATAINDIA", "BBTC", "BEL", "BEML", "BERGEPAINT", "BFUTILITIE", "BHARATFIN", "BHARATFORG", "BHARTIARTL", "BHEL", "BIOCON", "BLISSGVS", "BLKASHYAP", "BLUEDART", "BOSCHLTD", "BPCL", "BRITANNIA", "BSE", "BSOFT", "CADILAHC", "CAMLINFINE", "CANBK", "CANFINHOME", "CAPACITE", "CASTROLIND", "CDSL", "CEATLTD", "CENTRUM", "CENTURYPLY", "CENTURYTEX", "CEREBRAINT", "CESC", "CGCL", "CGPOWER", "CHENNPETRO", "CHOLAFIN", "CIPLA", "CNOVAPETRO", "COALINDIA"]
data = [{'tradable': True, 'mode': 'full', 'instrument_token': 121345, 'last_price': 21884.85, 'last_quantity': 1, 'average_price': 21847.28, 'volume': 458, 'buy_quantity': 1, 'sell_quantity': 0, 'ohlc': {'open': 22054.1, 'high': 22054.1, 'low': 21730.0, 'close': 21915.85}, 'change': -0.14145013768573886, 'last_trade_time': datetime.datetime(2019, 7, 19, 15, 29, 54), 'oi': 0, 'oi_day_high': 0, 'oi_day_low': 0, 'timestamp': datetime.datetime(2019, 7, 19, 17, 6, 26), 'depth': {'buy': [{'quantity': 1, 'price': 21884.85, 'orders': 1}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}], 'sell': [{'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}]}}, {'tradable': True, 'mode': 'full', 'instrument_token': 1793, 'last_price': 1638.7, 'last_quantity': 9, 'average_price': 1659.16, 'volume': 131464, 'buy_quantity': 566, 'sell_quantity': 0, 'ohlc': {'open': 9999999695.0, 'high': 1695.0, 'low': 1600.0, 'close': 1679.2}, 'change': -2.4118627918056217, 'last_trade_time': datetime.datetime(2019, 7, 19, 15, 29, 51), 'oi': 0, 'oi_day_high': 0, 'oi_day_low': 0, 'timestamp': datetime.datetime(2019, 7, 19, 17, 6, 26), 'depth': {'buy': [{'quantity': 566, 'price': 1638.7, 'orders': 6}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}], 'sell': [{'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}]}}, {'tradable': True, 'mode': 'full', 'instrument_token': 3038209, 'last_price': 96.9, 'last_quantity': 40, 'average_price': 98.69, 'volume': 64374, 'buy_quantity': 68, 'sell_quantity': 0, 'ohlc': {'open': 102.0, 'high': 102.45, 'low': 95.85, 'close': 100.0}, 'change': -3.0999999999999943, 'last_trade_time': datetime.datetime(2019, 7, 19, 15, 48, 39), 'oi': 0, 'oi_day_high': 0, 'oi_day_low': 0, 'timestamp': datetime.datetime(2019, 7, 19, 17, 6, 26), 'depth': {'buy': [{'quantity': 68, 'price': 96.9, 'orders': 2}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 999.7, 'orders': 0}], 'sell': [{'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 4.99999, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}]}}]
tick_dict = {'tradable': True, 'mode': 'full', 'instrument_token': 121345, 'last_price': 21884.85, 'last_quantity': 1, 'average_price': 21847.28, 'volume': 458, 'buy_quantity': 1, 'sell_quantity': 0, 'ohlc': {'open': 22054.1, 'high': 22054.1, 'low': 21730.0, 'close': 21915.85}, 'change': -0.14145013768573886, 'last_trade_time': datetime.datetime(2019, 7, 19, 15, 29, 54), 'oi': 0, 'oi_day_high': 0, 'oi_day_low': 0, 'timestamp': datetime.datetime(2019, 7, 19, 17, 6, 26), 'depth': {'buy': [{'quantity': 1, 'price': 21884.85, 'orders': 1}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}], 'sell': [{'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}, {'quantity': 0, 'price': 0.0, 'orders': 0}]}}


pprint(data[2]['depth']['buy'][4]['price'])


# pprint(tick_dict['mode'])
# pprint(data[0]['depth']['buy'][0]['price'])


# for name in tick_dict.keys():
# 	print(name)


# # pprint(data)
# # pprint (tick_dict['made'])
# pprint(tick_dict['mode'])
# # print (listofstocks[3])

# pprint(listofstocks[3])
# # print (tick_dict['last_price'])
# pprint(tick_dict['last_price'])


# homework: get all the points of company 1

# this will give all stocks

# for x in listofstocks:
#     print(x)

# # this will give all keys
# for y in tick_dict:
#     print(y)


# # # this will give all values
# for a in tick_dict:
#     print(tick_dict[a])

# # print ket=y and vlaue
# for b in tick_dict:
#     print(b, tick_dict[b])
