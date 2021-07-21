import datetime
import time
from kiteconnect import KiteConnect
from kiteconnect import exceptions
import json
import pdb
import pandas as pd
import xlwings as xw


ak = 'sp9kkdub3kf8qufe'
asecret = 'gkrkwqc96crjubarzg8ybbbbhbji1425'


kite = KiteConnect(api_key=ak)
request_tkn = input("[*] Enter Your Request Token Here : ")
data = kite.generate_session(request_tkn, api_secret=asecret)
kite.set_access_token(data["access_token"])
print(data['access_token'])
# kite.set_access_token('pQubf4c0dCCVhAtmvGyfipoLbqMWcuEd')

trd_portfolio = {}


wb = xw.Book('config.xlsx')


def read_excel():
    sht = wb.sheets['Sheet1']
    for x in range(1, 1000):
        val = sht.range('A'+str(x)).value
        if val == None:
            break
        name = val.split("/")[0]
        token = int(val.split("/")[1])
        trd_portfolio[name] = {"token": token}


read_excel()
sht2 = wb.sheets['Sheet2']
from_date = sht2.range('A1').value
to_date = sht2.range('A2').value
interval = sht2.range('A3').value

# pdb.set_trace()


print(f"dates are {from_date}----> {to_date} for {interval}")


for name in trd_portfolio:
    token = trd_portfolio[name]['token']
    records = kite.historical_data(token, from_date, to_date, interval)
    df = pd.DataFrame(records)
    df.to_csv(name+".csv")
    print(f"got data for {name}")
