from kiteconnect import KiteConnect
from kiteconnect import KiteTicker
import pandas as pd
import datetime
import pdb

kws = ""
kite = ""

api_k = "5t4uaet9jycxgcmu"  # api_key
api_s = "cydpv9svuw31wblnvxtt9b8xa1dlxcsy"  # api_secret


def get_login(api_k, api_s):  # log in to zerodha API panel
    global kws, kite
    kite = KiteConnect(api_key=api_k)

    print("[*] Generate access Token : ", kite.login_url())
    request_tkn = input("[*] Enter Your Request Token Here : ")
    data = kite.generate_session(request_tkn, api_secret=api_s)
    kite.set_access_token(data["access_token"])
    kws = KiteTicker(api_k, data["access_token"])
    print(data['access_token'])


get_login(api_k, api_s)
