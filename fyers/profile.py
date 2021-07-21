from session import fyers, token


profile = fyers. get_profile(token = token)
funds = fyers.funds(token = token)
print(funds)