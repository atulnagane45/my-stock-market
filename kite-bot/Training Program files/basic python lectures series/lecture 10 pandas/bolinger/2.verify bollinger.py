import easy_algo as ea
import pdb
import pandas as pd
import matplotlib.pyplot as plt
print("chnage portfolio")


# indicator..
# plot..
# pandas
# excel writing..

stocks_list = ['WIPRO', 'MFSL', 'RELIANCE', 'PCJEWELLER', 'BHEL', 'ALBK', 'TATACOMM', 'IOC', 'RPOWER', 'AJANTPHARM', 'MARUTI', 'TATAMTRDVR', 'EXIDEIND', 'ICICIBANK', 'MOTHERSUMI', 'INDIGO', 'AXISBANK', 'BOSCHLTD', 'BHARATFORG', 'NIITTECH', 'HEXAWARE', 'TCS', 'IDEA', 'DHFL', 'AMARAJABAT', 'GAIL', 'IFCI', 'TECHM', 'CONCOR', 'SUZLON', 'MINDTREE', 'ASHOKLEY', 'PFC', 'REPCOHOME', 'HDFC', 'RECLTD', 'TVSMOTOR', 'TATAMOTORS', 'JINDALSTEL', 'SRTRANSFIN', 'DCBBANK', 'ZEEL', 'ULTRACEMCO', 'CHENNPETRO', 'SOUTHBANK', 'RBLBANK', 'HINDALCO', 'GSFC', 'TV18BRDCST', 'RELCAPITAL', 'IRB', 'TITAN', 'SUNTV', 'CADILAHC', 'EICHERMOT', 'MCDOWELL-N', 'SAIL', 'BEML', 'MRPL', 'GLENMARK', 'CIPLA', 'IDFCFIRSTB', 'RAMCOCEM', 'CASTROLIND', 'GRASIM', 'INDIANB', 'IDFC', 'TATAPOWER', 'JUBLFOOD', 'LT', 'INFIBEAM', 'ORIENTBANK', 'MANAPPURAM', 'TATAELXSI', 'COLPAL', 'HDFCBANK', 'ITC', 'ASIANPAINT', 'AUROPHARMA', 'PEL', 'BRITANNIA', 'OIL', 'M&MFIN', 'APOLLOTYRE', 'SUNPHARMA', 'ENGINERSIN', 'CEATLTD', 'DLF', 'NESTLEIND', 'CANBK', 'NATIONALUM', 'ESCORTS', 'POWERGRID', 'GODFRYPHLP', 'GODREJCP', 'ONGC', 'MRF', 'BIOCON', 'M&M', 'DABUR', 'BHARTIARTL', 'UNIONBANK', 'NHPC', 'VOLTAS', 'BAJFINANCE', 'RELINFRA', 'BAJAJFINSV', 'VEDL', 'PVR', 'ACC', 'MGL', 'BPCL', 'NCC', 'STAR', 'HINDPETRO', 'HEROMOTOCO', 'UPL', 'IDBI', 'DRREDDY', 'BANKINDIA', 'NMDC', 'HCLTECH', 'DIVISLAB', 'L&TFH', 'CHOLAFIN', 'MCX', 'IBULHSGFIN', 'ARVIND', 'COALINDIA', 'TATASTEEL', 'INDUSINDBK', 'ADANIENT', 'SBIN', 'VGUARD', 'BAJAJ-AUTO', 'MUTHOOTFIN', 'KSCL', 'GODREJIND', 'LUPIN', 'RAYMOND', 'SHREECEM', 'BATAINDIA', 'KTKBANK', 'JSWSTEEL', 'GMRINFRA', 'TATAGLOBAL', 'HINDUNILVR', 'TORNTPOWER', 'TATACHEM', 'BERGEPAINT', 'BHARATFIN', 'SYNDIBANK', 'LICHSGFIN', 'CENTURYTEX', 'DISHTV', 'KOTAKBANK', 'JISLJALEQS', 'INFRATEL', 'UJJIVAN', 'TORNTPHARM', 'AMBUJACEM', 'BEL', 'YESBANK', 'BANKBARODA', 'NTPC', 'SRF', 'WOCKPHARMA', 'BALKRISIND', 'NBCC', 'INDIACEM', 'APOLLOHOSP', 'HINDZINC', 'CESC', 'FEDERALBNK', 'ADANIPORTS', 'IGL', 'ICICIPRULI', 'INFY', 'CUMMINSIND', 'CGPOWER', 'PNB', 'JUSTDIAL', 'OFSS', 'EQUITAS', 'SIEMENS', 'MARICO', 'UBL', 'PAGEIND', 'PIDILITIND', 'BSOFT', 'CANFINHOME', 'PETRONET', 'ADANIPOWER', 'HAVELLS', 'KAJARIACER', 'JETAIRWAYS']


for stock in stocks_list:

    data = ea.jsonreader(stock, "F:\\projects\\Softwares\\data storage\\1 day\\2005\\")
    df = pd.DataFrame(data)

    # print(df)

    df['mean'] = df['close'].rolling(20).mean()
    df['std'] = df['close'].rolling(20).std()

    df['upperband'] = df['mean'] + (df['std']*2)
    df['lowerband'] = df['mean'] - (df['std']*2)

    pdb.set_trace()
    df = df.drop(columns=['high', 'low', 'volume', 'mean', 'std', 'open'])

    df['date'] = pd.to_datetime(df['date'])

    df = df.set_index(['date'])
    df.plot()
    pdb.set_trace()
    plt.show()

    df.to_excel(str(stock)+".xlsx")


# import json

# computer_path = "E:\\data storage\\5 mins\\"
# stock = "ACC"


# def jsonreader(stock, computer_path):
#     path = computer_path + stock + '.json'
#     print("opening file:", stock)

#     with open(path, 'r') as f:
#         data = json.load(f)
#         return data


# ohlc = jsonreader(stock, computer_path=computer_path)
# print(ohlc)


# nsepy


# 1. x = high - low
# 2. average = mean(x)
# 3. list nifty 50 > find average of each

# ohlc x
