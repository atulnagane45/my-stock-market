from kiteconnect import KiteConnect
from kiteconnect import KiteTicker
import pandas as pd
import datetime
import pdb
from pandas.io.json import json_normalize
kws = ""
kite = ""

api_k = "sp9kkdub3kf8qufe"  # api_key
api_s = "gkrkwqc96crjubarzg8ybbbbhbji1425"  # api_secret
access_token = "VGNS9VT1F6YFPkghboqz8z5ekvUt9gBe"


def get_login(api_k, api_s):  # log in to zerodha API panel
    global kws, kite
    kite = KiteConnect(api_key=api_k)

    # print("[*] Generate access Token : ", kite.login_url())
    # request_tkn = input("[*] Enter Your Request Token Here : ")
    # data = kite.generate_session(request_tkn, api_secret=api_s)
    # kite.set_access_token(data["access_token"])
    # kws = KiteTicker(api_k, data["access_token"])
    # print(data['access_token'])

    kite.set_access_token(access_token)
    kws = KiteTicker(api_k, access_token)


get_login(api_k, api_s)

trd_portfolio = {7455745: "PCJEWELLER", 5633: "ACC", 975873: "ZEEL", 13992450: "BANKNIFTY19AUGFUT"}


def algo1():
    pass


def on_ticks(ws, ticks):
    for single_comapny in ticks:

        inst_of_single_company = single_comapny['instrument_token']
        name = trd_portfolio[inst_of_single_company]

        print(single_comapny, name)
        print(json_normalize(single_comapny))
        pdb.set_trace()

    print("\n")


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
inst_token = [7455745, 5633, 975873, 13992450]


def on_connect(ws, response):
    ws.subscribe(inst_token)
    ws.set_mode(ws.MODE_FULL, inst_token)


kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.connect()
