import pdb
import pickle
import json
import datetime

trd_portfolio = {}

# ---------------------------------------------------------------------------------------------------------------------------------------------------------


def test():
    print("sucessfully imported")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------


def buy(buying_price, stoploss, time, rpt, verbose):

    quantity = int(rpt / (buying_price - stoploss))
    specs = {'buying_price': buying_price, 'stoploss': stoploss,
             'time': time, 'status': 'bought', 'quantity': quantity}

    if verbose == 'True':
        print("\n", specs)
    print("returning specs")
    return specs

# ---------------------------------------------------------------------------------------------------------------------------------------------------------


def sell(selling_price, stoploss, time, rpt, verbose):

    quantity = int(rpt / (stoploss - selling_price))
    specs = {'selling_price': selling_price, 'stoploss': stoploss,
             'time': time, 'status': 'sold', 'quantity': quantity}

    if verbose == 'True':
        print("\n", specs)
    print("returning specs")
    return specs

# ---------------------------------------------------------------------------------------------------------------------------------------------------------


def buy_stoploss_hit_checker(row_no, current_low, stoploss_value, buying_price_value, quantity_value, times, market_over, close_value):

    if current_low < stoploss_value:
        pnl = (stoploss_value - buying_price_value) * quantity_value
        print("\t", "stoploss hit:", times, "pnl:", pnl)
        excel_writer(row_no=row_no, values={
                     'pnl': pnl, 'exit': stoploss_value, 'exit_time': times})
        return "stoploss_hit"

    if market_over == "yes":
        pnl = (close_value - buying_price_value) * quantity_value
        print("\t", "market over:", times, "pnl:", pnl)
        excel_writer(row_no=row_no, values={
                     'pnl': pnl, 'exit': close_value, 'exit_time': times})

# ---------------------------------------------------------------------------------------------------------------------------------------------------------


def checkstoploss(specs, minute, verbose, market_over):

    if specs['status'] == 'bought':
        if minute['low'] < specs['stoploss']:
            pnl = (specs['stoploss'] - specs['buying_price']) * \
                specs['quantity']
            if verbose == 'True':
                print("\t", "for buy stoploss hit:",
                      minute['date'], "pnl:", pnl)

            specs = specs.update({'stoploss_hit': 'yes', 'stoploss_hit_time': minute[
                                 'date'], 'status': 'stoploss_hit', 'pnl': pnl})
            return specs

        if market_over == 'yes':
            pnl = (minute['close'] - specs['buying_price']) * specs['quantity']

            if verbose == 'True':
                print("\t", "for buy market over:",
                      minute['date'], "pnl:", pnl)

            specs = specs.update({'stoploss_hit': 'yes', 'stoploss_hit_time': minute[
                                 'date'], 'status': 'market_over', 'pnl': pnl})
            return specs

    if specs['status'] == 'sold':
        if minute['high'] > specs['stoploss']:
            pnl = (specs['selling_price'] - specs['stoploss']) * \
                specs['quantity']

            if verbose == 'True':
                print("\t", "for sell stoploss hit:",
                      minute['date'], "pnl:", pnl)

            specs = specs.update({'stoploss_hit': 'yes', 'stoploss_hit_time': minute[
                                 'date'], 'status': 'stoploss_hit', 'pnl': pnl})
            return specs

        if market_over == 'yes':
            pnl = (specs['selling_price'] - minute['close']) * \
                specs['quantity']

            if verbose == 'True':
                print("\t", "for sell market over:",
                      minute['date'], "pnl:", pnl)

            specs = specs.update({'stoploss_hit': 'yes', 'stoploss_hit_time': minute[
                                 'date'], 'status': 'market_over', 'pnl': pnl})
            return specs

# ---------------------------------------------------------------------------------------------------------------------------------------------------------


def str_to_datetime(date_string):
    date_string = date_string[:16]
    date_datetime = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M')
    return date_datetime

# ---------------------------------------------------------------------------------------------------------------------------------------------------------


def portfolio(stocks, file_required):

    # check code for select tokens for fno
    # check code when file_required= new
    # stocks is a list

    if file_required == 'new':
        print("waiting for data from zerodha")
        inst = kite.instruments()  # on when pn aws
        print("got data from zerodha")

        # with open('instuments.pickle','wb') as f:
        #    pickle.dump(inst, f)

    if file_required == 'old_will_work':
        pickle_in = open('instuments.pickle', 'rb')
        inst = pickle.load(pickle_in)

    for stock_name in stocks:
        for stock in inst:
            if stock['tradingsymbol'] == str(stock_name) and stock['instrument_type'] == "FUT" and stock['exchange'] == 'NFO':
                trd_portfolio[stock_name] = {
                    'token': stock['instrument_token']}

            if stock['tradingsymbol'] == str(stock_name) and stock['instrument_type'] == "EQ" and stock['exchange'] == 'NSE':
                trd_portfolio[stock_name] = {
                    'token': stock['instrument_token']}

    return trd_portfolio

# ---------------------------------------------------------------------------------------------------------------------------------------------------------


def jsonreader(stock, computer_path):
    path = computer_path + stock + '.json'
    print("opening file:", stock)
    with open(path, 'r') as f:
        data = json.load(f)
        return data

# ---------------------------------------------------------------------------------------------------------------------------------------------------------


def bolliger_band(df):

    df['mean'] = df['close'].rolling(20).mean()
    df['std'] = df['close'].rolling(20).std()

    df['upperband'] = df['mean'] + (df['std'] * 2)
    df['lowerband'] = df['mean'] - (df['std'] * 2)
    df = df.drop(['mean', 'std'], axis=1)
    return df

# ---------------------------------------------------------------------------------------------------------------------------------------------------------


def rsi(df):
    df['change'] = df['close'].diff()

    def gain(x):
        if x > 0:
            return x
        else:
            return 0

    def loss(x):
        if x < 0:
            return x
        else:
            return 0

    df['gain'] = df['change'].apply(gain)
    df['loss'] = abs(df['change'].apply(loss))
    df['average_gain'] = df['gain'].rolling(14).mean()
    df['average_loss'] = df['loss'].rolling(14).mean()
    df['rs'] = df['average_gain'] / df['average_loss']
    df['rsi'] = (100 - (100 / (1 + df['rs'])))
    df = df.drop(['change', 'gain', 'loss', 'average_gain',
                  'average_loss', 'rs'], axis=1)
    return df
