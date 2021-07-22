from kiteconnect import KiteConnect

import pdb

api_key = " "  # id
#api_secret = "gkrkwqc96crjubarzg8ybbbbhbji1425"  # pass
# request_token = "bB3Cy7vmPrLzyg9eGFHJylFTaPzbz5nE"  # otp


# access_token = "1elrkM2JvDai4suWD5LuIucnnqgv3mP0"

kite = KiteConnect(api_key=api_key)
# data = kite.generate_session(request_token, api_secret=api_secret)

pdb.set_trace()
kite.set_access_token(access_token)


# print(data)
print(kite.orders())

kite.place_order(tradingsymbol='CIPLA', price=552, variety=kite.VARIETY_BO, exchange=kite.EXCHANGE_NSE, transaction_type=kite.TRANSACTION_TYPE_BUY, quantity=100, squareoff=10, stoploss=5, order_type=kite.ORDER_TYPE_LIMIT, product=kite.PRODUCT_BO)
