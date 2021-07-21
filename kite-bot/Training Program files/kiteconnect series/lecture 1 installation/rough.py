from kiteconnect import KiteConnect

import pdb

api_key = "sp9kkdub3kf8qufe"  # id
api_secret = "gkrkwqc96crjubarzg8ybbbbhbji1425"  # pass
access_token = "8ZN453ZmcAlTNSOWSxSaPPhhBmJ6ZQk3"

kite = KiteConnect(api_key=api_key)
# data = kite.generate_session(request_token, api_secret=api_secret)
kite.set_access_token(access_token)


pdb.set_trace()
print(kite.orders())
kite.place_order(tradingsymbol='CIPLA', price=552, variety=kite.VARIETY_BO, exchange=kite.EXCHANGE_NSE, transaction_type=kite.TRANSACTION_TYPE_BUY, quantity=10, squareoff=10, stoploss=5, order_type=kite.ORDER_TYPE_LIMIT, product=kite.PRODUCT_BO)
kite.exit_order(variety=kite.VARIETY_BO, order_id=190913002598525)
