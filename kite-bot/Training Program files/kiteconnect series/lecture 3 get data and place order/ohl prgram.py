from kiteconnect import KiteConnect
from kiteconnect import KiteTicker
import pandas as pd
import datetime
import pdb

kws = ""
kite = ""

api_k = "sp9kkdub3kf8qufe"  # api_key
api_s = "gkrkwqc96crjubarzg8ybbbbhbji1425"  # api_secret
access_token = "8ZN453ZmcAlTNSOWSxSaPPhhBmJ6ZQk3"


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

# trd_portfolio = {969473: 'WIPRO', 548353: 'MFSL', 738561: 'RELIANCE', 7455745: 'PCJEWELLER', 112129: 'BHEL', 2760193: 'ALBK', 952577: 'TATACOMM', 415745: 'IOC', 3906305: 'RPOWER', 2079745: 'AJANTPHARM', 2815745: 'MARUTI', 4343041: 'TATAMTRDVR', 173057: 'EXIDEIND', 1270529: 'ICICIBANK', 1076225: 'MOTHERSUMI', 2865921: 'INDIGO', 1510401: 'AXISBANK', 558337: 'BOSCHLTD', 108033: 'BHARATFORG', 2955009: 'NIITTECH', 2747905: 'HEXAWARE', 2953217: 'TCS', 3677697: 'IDEA', 215553: 'DHFL', 25601: 'AMARAJABAT', 1207553: 'GAIL', 381697: 'IFCI', 3465729: 'TECHM', 1215745: 'CONCOR', 3076609: 'SUZLON', 3675137: 'MINDTREE', 54273: 'ASHOKLEY', 3660545: 'PFC', 7577089: 'REPCOHOME', 340481: 'HDFC', 3930881: 'RECLTD', 2170625: 'TVSMOTOR', 884737: 'TATAMOTORS', 1723649: 'JINDALSTEL', 1102337: 'SRTRANSFIN', 3513601: 'DCBBANK', 975873: 'ZEEL', 2952193: 'ULTRACEMCO', 524545: 'CHENNPETRO', 1522689: 'SOUTHBANK', 4708097: 'RBLBANK', 348929: 'HINDALCO', 319233: 'GSFC', 3637249: 'TV18BRDCST', 737793: 'RELCAPITAL', 3920129: 'IRB', 897537: 'TITAN', 3431425: 'SUNTV', 2029825: 'CADILAHC', 232961: 'EICHERMOT', 2674433: 'MCDOWELL-N', 758529: 'SAIL', 101121: 'BEML', 584449: 'MRPL', 1895937: 'GLENMARK', 177665: 'CIPLA', 2863105: 'IDFCFIRSTB', 523009: 'RAMCOCEM', 320001: 'CASTROLIND', 315393: 'GRASIM', 3663105: 'INDIANB', 3060993: 'IDFC', 877057: 'TATAPOWER', 4632577: 'JUBLFOOD', 2939649: 'LT', 4159745: 'INFIBEAM', 636673: 'ORIENTBANK', 4879617: 'MANAPPURAM', 873217: 'TATAELXSI', 3876097: 'COLPAL', 341249: 'HDFCBANK', 424961: 'ITC', 60417: 'ASIANPAINT', 70401: 'AUROPHARMA', 617473: 'PEL', 140033: 'BRITANNIA', 4464129: 'OIL', 3400961: 'M&MFIN', 41729: 'APOLLOTYRE', 857857: 'SUNPHARMA', 1256193: 'ENGINERSIN', 3905025: 'CEATLTD', 3771393: 'DLF', 4598529: 'NESTLEIND', 2763265: 'CANBK', 1629185: 'NATIONALUM', 245249: 'ESCORTS', 3834113: 'POWERGRID', 302337: 'GODFRYPHLP', 2585345: 'GODREJCP', 633601: 'ONGC', 582913: 'MRF', 2911489: 'BIOCON', 519937: 'M&M', 197633: 'DABUR', 2714625: 'BHARTIARTL', 2752769: 'UNIONBANK', 4454401: 'NHPC', 951809: 'VOLTAS', 81153: 'BAJFINANCE', 141569: 'RELINFRA', 4268801: 'BAJAJFINSV', 784129: 'VEDL', 3365633: 'PVR', 5633: 'ACC', 4488705: 'MGL', 134657: 'BPCL', 593665: 'NCC', 1887745: 'STAR', 359937: 'HINDPETRO', 345089: 'HEROMOTOCO', 2889473: 'UPL', 377857: 'IDBI', 225537: 'DRREDDY', 1214721: 'BANKINDIA', 3924993: 'NMDC', 1850625: 'HCLTECH', 2800641: 'DIVISLAB', 6386689: 'L&TFH', 175361: 'CHOLAFIN', 7982337: 'MCX', 7712001: 'IBULHSGFIN', 49409: 'ARVIND', 5215745: 'COALINDIA', 895745: 'TATASTEEL', 1346049: 'INDUSINDBK', 6401: 'ADANIENT', 779521: 'SBIN', 3932673: 'VGUARD', 4267265: 'BAJAJ-AUTO', 6054401: 'MUTHOOTFIN', 3832833: 'KSCL', 2796801: 'GODREJIND', 2672641: 'LUPIN', 731905: 'RAYMOND', 794369: 'SHREECEM', 94977: 'BATAINDIA', 2061825: 'KTKBANK', 3001089: 'JSWSTEEL', 3463169: 'GMRINFRA', 878593: 'TATAGLOBAL', 356865: 'HINDUNILVR', 3529217: 'TORNTPOWER', 871681: 'TATACHEM', 103425: 'BERGEPAINT', 4995329: 'BHARATFIN', 1837825: 'SYNDIBANK', 511233: 'LICHSGFIN', 160001: 'CENTURYTEX', 3721473: 'DISHTV', 492033: 'KOTAKBANK', 2661633: 'JISLJALEQS', 7458561: 'INFRATEL', 4369665: 'UJJIVAN', 900609: 'TORNTPHARM', 325121: 'AMBUJACEM', 98049: 'BEL', 3050241: 'YESBANK', 1195009: 'BANKBARODA', 2977281: 'NTPC', 837889: 'SRF', 1921537: 'WOCKPHARMA', 85761: 'BALKRISIND', 8042241: 'NBCC', 387841: 'INDIACEM', 40193: 'APOLLOHOSP', 364545: 'HINDZINC', 160769: 'CESC', 261889: 'FEDERALBNK', 3861249: 'ADANIPORTS', 2883073: 'IGL', 4774913: 'ICICIPRULI', 408065: 'INFY', 486657: 'CUMMINSIND', 194561: 'CGPOWER', 2730497: 'PNB', 7670273: 'JUSTDIAL', 2748929: 'OFSS', 4314113: 'EQUITAS', 806401: 'SIEMENS', 1041153: 'MARICO', 4278529: 'UBL', 3689729: 'PAGEIND', 681985: 'PIDILITIND', 1790465: 'BSOFT', 149249: 'CANFINHOME', 2905857: 'PETRONET', 4451329: 'ADANIPOWER', 2513665: 'HAVELLS', 462849: 'KAJARIACER', 2997505: 'JETAIRWAYS'}
trd_portfolio = {969473: {"name": 'WIPRO'}, 548353: {"name": 'MFSL'}, 738561: {"name": 'RELIANCE'}, 7455745: {"name": 'PCJEWELLER'}, 112129: {"name": 'BHEL'}, 2760193: {"name": 'ALBK'}, 952577: {"name": 'TATACOMM'}, 415745: {"name": 'IOC'}, 3906305: {"name": 'RPOWER'}, 2079745: {"name": 'AJANTPHARM'}, 2815745: {"name": 'MARUTI'}, 4343041: {"name": 'TATAMTRDVR'}, 173057: {"name": 'EXIDEIND'}, 1270529: {"name": 'ICICIBANK'}, 1076225: {"name": 'MOTHERSUMI'}, 2865921: {"name": 'INDIGO'}, 1510401: {"name": 'AXISBANK'}, 558337: {"name": 'BOSCHLTD'}, 108033: {"name": 'BHARATFORG'}, 2955009: {"name": 'NIITTECH'}, 2747905: {"name": 'HEXAWARE'}, 2953217: {"name": 'TCS'}, 3677697: {"name": 'IDEA'}, 215553: {"name": 'DHFL'}, 25601: {"name": 'AMARAJABAT'}, 1207553: {"name": 'GAIL'}, 381697: {"name": 'IFCI'}, 3465729: {"name": 'TECHM'}, 1215745: {"name": 'CONCOR'}, 3076609: {"name": 'SUZLON'}, 3675137: {"name": 'MINDTREE'}, 54273: {"name": 'ASHOKLEY'}, 3660545: {"name": 'PFC'}, 7577089: {"name": 'REPCOHOME'}, 340481: {"name": 'HDFC'}, 3930881: {"name": 'RECLTD'}, 2170625: {"name": 'TVSMOTOR'}, 884737: {"name": 'TATAMOTORS'}, 1723649: {"name": 'JINDALSTEL'}, 1102337: {"name": 'SRTRANSFIN'}, 3513601: {"name": 'DCBBANK'}, 975873: {"name": 'ZEEL'}, 2952193: {"name": 'ULTRACEMCO'}, 524545: {"name": 'CHENNPETRO'}, 1522689: {"name": 'SOUTHBANK'}, 4708097: {"name": 'RBLBANK'}, 348929: {"name": 'HINDALCO'}, 319233: {"name": 'GSFC'}, 3637249: {"name": 'TV18BRDCST'}, 737793: {"name": 'RELCAPITAL'}, 3920129: {"name": 'IRB'}, 897537: {"name": 'TITAN'}, 3431425: {"name": 'SUNTV'}, 2029825: {"name": 'CADILAHC'}, 232961: {"name": 'EICHERMOT'}, 2674433: {"name": 'MCDOWELL-N'}, 758529: {"name": 'SAIL'}, 101121: {"name": 'BEML'}, 584449: {"name": 'MRPL'}, 1895937: {"name": 'GLENMARK'}, 177665: {"name": 'CIPLA'}, 2863105: {"name": 'IDFCFIRSTB'}, 523009: {"name": 'RAMCOCEM'}, 320001: {"name": 'CASTROLIND'}, 315393: {"name": 'GRASIM'}, 3663105: {"name": 'INDIANB'}, 3060993: {"name": 'IDFC'}, 877057: {"name": 'TATAPOWER'}, 4632577: {"name": 'JUBLFOOD'}, 2939649: {"name": 'LT'}, 4159745: {"name": 'INFIBEAM'}, 636673: {"name": 'ORIENTBANK'}, 4879617: {"name": 'MANAPPURAM'}, 873217: {"name": 'TATAELXSI'}, 3876097: {"name": 'COLPAL'}, 341249: {"name": 'HDFCBANK'}, 424961: {"name": 'ITC'}, 60417: {"name": 'ASIANPAINT'}, 70401: {"name": 'AUROPHARMA'}, 617473: {"name": 'PEL'}, 140033: {"name": 'BRITANNIA'}, 4464129: {"name": 'OIL'}, 3400961: {"name": 'M&MFIN'}, 41729: {"name": 'APOLLOTYRE'}, 857857: {"name": 'SUNPHARMA'}, 1256193: {"name": 'ENGINERSIN'}, 3905025: {"name": 'CEATLTD'}, 3771393: {"name": 'DLF'}, 4598529: {"name": 'NESTLEIND'}, 2763265: {"name": 'CANBK'}, 1629185: {"name": 'NATIONALUM'}, 245249: {"name": 'ESCORTS'}, 3834113: {"name": 'POWERGRID'}, 302337: {"name": 'GODFRYPHLP'}, 2585345: {"name": 'GODREJCP'}, 633601: {"name": 'ONGC'}, 582913: {"name": 'MRF'}, 2911489: {"name": 'BIOCON'}, 519937: {"name": 'M&M'}, 197633: {"name": 'DABUR'}, 2714625: {"name": 'BHARTIARTL'}, 2752769: {"name": 'UNIONBANK'}, 4454401: {"name": 'NHPC'}, 951809: {"name": 'VOLTAS'}, 81153: {"name": 'BAJFINANCE'}, 141569: {"name": 'RELINFRA'}, 4268801: {"name": 'BAJAJFINSV'}, 784129: {"name": 'VEDL'}, 3365633: {"name": 'PVR'}, 5633: {"name": 'ACC'}, 4488705: {"name": 'MGL'}, 134657: {"name": 'BPCL'}, 593665: {"name": 'NCC'}, 1887745: {"name": 'STAR'}, 359937: {"name": 'HINDPETRO'}, 345089: {"name": 'HEROMOTOCO'}, 2889473: {"name": 'UPL'}, 377857: {"name": 'IDBI'}, 225537: {"name": 'DRREDDY'}, 1214721: {"name": 'BANKINDIA'}, 3924993: {"name": 'NMDC'}, 1850625: {"name": 'HCLTECH'}, 2800641: {"name": 'DIVISLAB'}, 6386689: {"name": 'L&TFH'}, 175361: {"name": 'CHOLAFIN'}, 7982337: {"name": 'MCX'}, 7712001: {"name": 'IBULHSGFIN'}, 49409: {"name": 'ARVIND'}, 5215745: {"name": 'COALINDIA'}, 895745: {"name": 'TATASTEEL'}, 1346049: {"name": 'INDUSINDBK'}, 6401: {"name": 'ADANIENT'}, 779521: {"name": 'SBIN'}, 3932673: {"name": 'VGUARD'}, 4267265: {"name": 'BAJAJ-AUTO'}, 6054401: {"name": 'MUTHOOTFIN'}, 3832833: {"name": 'KSCL'}, 2796801: {"name": 'GODREJIND'}, 2672641: {"name": 'LUPIN'}, 731905: {"name": 'RAYMOND'}, 794369: {"name": 'SHREECEM'}, 94977: {"name": 'BATAINDIA'}, 2061825: {"name": 'KTKBANK'}, 3001089: {"name": 'JSWSTEEL'}, 3463169: {"name": 'GMRINFRA'}, 878593: {"name": 'TATAGLOBAL'}, 356865: {"name": 'HINDUNILVR'}, 3529217: {"name": 'TORNTPOWER'}, 871681: {"name": 'TATACHEM'}, 103425: {"name": 'BERGEPAINT'}, 4995329: {"name": 'BHARATFIN'}, 1837825: {"name": 'SYNDIBANK'}, 511233: {"name": 'LICHSGFIN'}, 160001: {"name": 'CENTURYTEX'}, 3721473: {"name": 'DISHTV'}, 492033: {"name": 'KOTAKBANK'}, 2661633: {"name": 'JISLJALEQS'}, 7458561: {"name": 'INFRATEL'}, 4369665: {"name": 'UJJIVAN'}, 900609: {"name": 'TORNTPHARM'}, 325121: {"name": 'AMBUJACEM'}, 98049: {"name": 'BEL'}, 3050241: {"name": 'YESBANK'}, 1195009: {"name": 'BANKBARODA'}, 2977281: {"name": 'NTPC'}, 837889: {"name": 'SRF'}, 1921537: {"name": 'WOCKPHARMA'}, 85761: {"name": 'BALKRISIND'}, 8042241: {"name": 'NBCC'}, 387841: {"name": 'INDIACEM'}, 40193: {"name": 'APOLLOHOSP'}, 364545: {"name": 'HINDZINC'}, 160769: {"name": 'CESC'}, 261889: {"name": 'FEDERALBNK'}, 3861249: {"name": 'ADANIPORTS'}, 2883073: {"name": 'IGL'}, 4774913: {"name": 'ICICIPRULI'}, 408065: {"name": 'INFY'}, 486657: {"name": 'CUMMINSIND'}, 194561: {"name": 'CGPOWER'}, 2730497: {"name": 'PNB'}, 7670273: {"name": 'JUSTDIAL'}, 2748929: {"name": 'OFSS'}, 4314113: {"name": 'EQUITAS'}, 806401: {"name": 'SIEMENS'}, 1041153: {"name": 'MARICO'}, 4278529: {"name": 'UBL'}, 3689729: {"name": 'PAGEIND'}, 681985: {"name": 'PIDILITIND'}, 1790465: {"name": 'BSOFT'}, 149249: {"name": 'CANFINHOME'}, 2905857: {"name": 'PETRONET'}, 4451329: {"name": 'ADANIPOWER'}, 2513665: {"name": 'HAVELLS'}, 462849: {"name": 'KAJARIACER'}, 2997505: {"name": 'JETAIRWAYS'}}
print(trd_portfolio)
# ----------------------------------------------------------
# 1. take data for 500 stocks ... (big_data 500 companies): done
# 2. take single_comapny data: done
# 3. acess its open high and low value
# 4. if open = low:
# place buy order
# 6. if open = high:
#     place sell order
# ----------------------------------------------------------


def on_ticks(ws, ticks):
    print("\n")
    for single_comapny in ticks:
        token = single_comapny['instrument_token']
        name = trd_portfolio[token]['name']

        openx = single_comapny['ohlc']['open']
        high = single_comapny['ohlc']['high']
        low = single_comapny['ohlc']['low']
        close = single_comapny['ohlc']['close']

        if (openx == low) and ("status" not in trd_portfolio[token].keys()):
            print(f"place buy order for {name}")
            trd_portfolio[token]['status'] = "traded"
            # pdb.set_trace()

        if openx == high and ("status" not in trd_portfolio[token].keys()):
            print(f"place sell order for {name}")
            trd_portfolio[token]['status'] = "traded"


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
inst_token = [x for x in trd_portfolio]


def on_connect(ws, response):
    ws.subscribe(inst_token)
    ws.set_mode(ws.MODE_QUOTE, inst_token)


# Assign the callbacks.
kws.on_ticks = on_ticks
kws.on_connect = on_connect

# Infinite loop on the main thread. Nothing after this will run.
# You have to use the pre-defined callbacks to manage subscriptions.
kws.connect()
