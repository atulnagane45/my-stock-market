stocks_to_trade = ['ADANIPORTS', 'ADANIPOWER', 'APOLLOTYRE', 'BANKBARODA', 'BANKINDIA', 'TORNTPOWER', 'UJJIVAN', 'UNIONBANK', 'VIPIND', 'VEDL', 'VOLTAS', 'YESBANK']

create list of stocks to trade

print(stocks_to_trade[1])

stocks_to_trade[0]

change values at index: if we want to replace it

stocks_to_trade[-1]: get last value

Indexerror: this eoorr may come

stocks_to_trade[:3]: top 3 stocks

stocks_to_trade[1:3]:

stocks_to_trade[:3]: last 3 stocks

stocks_to_trade[1:]: leave the first one

stocks_to_trade.append("CIPLA"): add stocks in live market

stocks_to_trade.romove("ACC"): if you dont want it to be traded now

stocks_to_trade.pop(): remove last stocks

stocks_to_trade.sort(): top gainer and looser.... mix with slicing

stocks_to_trade.sort(reverse=True): for top looser.... mix with slicing

stocks_to_trade.min()... lowest stock for the day

stocks_to_trade.max()... highest stock

stocks_to_trade.sum()... total pnl..

stocks_to_trade.index("ADANIPORTS")...

"ZEEL" in stocks_to_trade... if already traded or not

for stock in stocks_to_trade:
    ... trade bit by bit
    print(stock)
