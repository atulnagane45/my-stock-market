import pdb
from nsepy import get_history
from datetime import date, timedelta
import pandas as pd
import xlwings as xw
import pickle
from nsepy.derivatives import get_expiry_date

wb = xw.Book('Algo trading.xlsx')

# this file will output pickle contailing average for equity
equity_sheet = wb.sheets['Equity']
end = date.today()
start = end - timedelta(days=10)

trd_portfolio = {}
for x in range(2, 200):
    inst = equity_sheet.range('A' + str(x)).value

    if inst == None:
        break

    quantity = int(equity_sheet.range('B' + str(x)).value)
    trd_portfolio[str(inst)] = {}
    trd_portfolio[str(inst)]['row'] = x
    trd_portfolio[str(inst)]['quantity'] = quantity
