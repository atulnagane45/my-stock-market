from fyers_api import fyersModel


access_token = 'gAAAAABg-RE7Phwf8_DUfBUJ9DDXWxdKRo_WYGulQDvfrzrGGKjPj_7rGwD_Qo-q-D6otL4evIypE_2Tm4UX4kAg3lXyIL6a3OWFU45tx9r1QZ5MibBxH4I=&user_id=XA08240&poa_flag=N'
token = access_token
is_async = False #(By default False, Change to True for asnyc API calls.)

fyers = fyersModel.FyersModel(is_async)

