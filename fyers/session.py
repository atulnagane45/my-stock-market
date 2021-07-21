from fyers_api import fyersModel


access_token = 'gAAAAABg-Fm1nXjVsPgymorhhg62S7XkZVt5k8uPhra-OaMflkAJUurfPKdcF9t8umMBZFdknFfr7kORvqgdyQ2GhDaEHDVNuKf9jYLAQlVuD5hqhrQ8OHg=&user_id=XA08240&poa_flag=N'
token = access_token
is_async = False #(By default False, Change to True for asnyc API calls.)

fyers = fyersModel.FyersModel(is_async)

