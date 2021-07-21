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


equity_dict = {}

for x in trd_portfolio:
    print(x)
    data = get_history(symbol=x, start=start, end=end)
    data = data[-5:]
    data['high-open'] = data['High'] - data['Open']
    data['open-low'] = data['Open'] - data['Low']
    data['min'] = data[['high-open', 'open-low']].min(axis=1)
    average = round(data['min'].mean(), 2)
    row_val = trd_portfolio[x]['row']
    equity_sheet.range('C' + str(row_val)).value = average

    if average > 1:
        equity_dict[x] = {'average': average, 'quantity': trd_portfolio[x]['quantity']}
        # pdb.set_trace()

print(equity_dict)
file_Name = open("equity_dict.pickle", "wb")
pickle.dump(equity_dict, file_Name)
file_Name.close()
print(equity_dict)
