#!python
import xlwings as xw
from pprint import pprint
import pdb
import pandas as pd
import logging
from kiteconnect import KiteTicker


kws = KiteTicker("5t4uaet9jycxgcmu", "1Pv0InM7Ph1ALEd69XeYxk6vMdOxC79R")


wb = xw.Book('live data.xlsx')
sht2 = wb.sheets['Sheet1']
data = sht2.range('A1').expand().value


def on_ticks(ws, ticks):
    pprint(ticks)

    pdb.set_trace()


def on_connect(ws, response):
    ws.subscribe([177665, 667468684])
    ws.set_mode(ws.MODE_QUOTE, [177665])


kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.connect()
