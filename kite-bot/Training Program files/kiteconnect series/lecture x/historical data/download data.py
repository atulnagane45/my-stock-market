import datetime
import time
from kiteconnect import KiteConnect
from kiteconnect import exceptions
import json

tdelta0 = datetime.timedelta(days=30)
tdelta = datetime.timedelta(days=29)
interval = "minute"
repeatation = 1

ak = '5t4uaet9jycxgcmu'
asecret = 'cydpv9svuw31wblnvxtt9b8xa1dlxcsy'


kite = KiteConnect(api_key=ak)
# request_tkn = input("[*] Enter Your Request Token Here : ");
# data = kite.generate_session(request_tkn, api_secret=asecret)
# kite.set_access_token(data["access_token"])
# print(data['access_token'])
kite.set_access_token('pQubf4c0dCCVhAtmvGyfipoLbqMWcuEd')


savedata = {}


def get_historical_data(instrument_token):
    return kite.historical(instrument_token, from_date, to_date, interval)


trd_portfolio = {'WIPRO': {'token': 969473}, 'MFSL': {'token': 548353}, 'RELIANCE': {'token': 738561}, 'PCJEWELLER': {'token': 7455745}, 'BHEL': {'token': 112129}, 'ALBK': {'token': 2760193}, 'TATACOMM': {'token': 952577}, 'IOC': {'token': 415745}, 'RPOWER': {'token': 3906305}, 'AJANTPHARM': {'token': 2079745}, 'MARUTI': {'token': 2815745}, 'TATAMTRDVR': {'token': 4343041}, 'EXIDEIND': {'token': 173057}, 'ICICIBANK': {'token': 1270529}, 'MOTHERSUMI': {'token': 1076225}, 'INDIGO': {'token': 2865921}, 'AXISBANK': {'token': 1510401}, 'BOSCHLTD': {'token': 558337}, 'BHARATFORG': {'token': 108033}, 'NIITTECH': {'token': 2955009}, 'HEXAWARE': {'token': 2747905}, 'TCS': {'token': 2953217}, 'IDEA': {'token': 3677697}, 'DHFL': {'token': 215553}, 'AMARAJABAT': {'token': 25601}, 'GAIL': {'token': 1207553}, 'IFCI': {'token': 381697}, 'TECHM': {'token': 3465729}, 'CONCOR': {'token': 1215745}, 'SUZLON': {'token': 3076609}, 'MINDTREE': {'token': 3675137}, 'ASHOKLEY': {'token': 54273}, 'PFC': {'token': 3660545}, 'REPCOHOME': {'token': 7577089}, 'HDFC': {'token': 340481}, 'RECLTD': {'token': 3930881}, 'TVSMOTOR': {'token': 2170625}, 'TATAMOTORS': {'token': 884737}, 'JINDALSTEL': {'token': 1723649}, 'SRTRANSFIN': {'token': 1102337}, 'DCBBANK': {'token': 3513601}, 'ZEEL': {'token': 975873}, 'ULTRACEMCO': {'token': 2952193}, 'CHENNPETRO': {'token': 524545}, 'SOUTHBANK': {'token': 1522689}, 'RBLBANK': {'token': 4708097}, 'HINDALCO': {'token': 348929}, 'GSFC': {'token': 319233}, 'TV18BRDCST': {'token': 3637249}, 'RELCAPITAL': {'token': 737793}, 'IRB': {'token': 3920129}, 'TITAN': {'token': 897537}, 'SUNTV': {'token': 3431425}, 'CADILAHC': {'token': 2029825}, 'EICHERMOT': {'token': 232961}, 'MCDOWELL-N': {'token': 2674433}, 'SAIL': {'token': 758529}, 'BEML': {'token': 101121}, 'MRPL': {'token': 584449}, 'GLENMARK': {'token': 1895937}, 'CIPLA': {'token': 177665}, 'IDFCFIRSTB': {'token': 2863105}, 'RAMCOCEM': {'token': 523009}, 'CASTROLIND': {'token': 320001}, 'GRASIM': {'token': 315393}, 'INDIANB': {'token': 3663105}, 'IDFC': {'token': 3060993}, 'TATAPOWER': {'token': 877057}, 'JUBLFOOD': {'token': 4632577}, 'LT': {'token': 2939649}, 'INFIBEAM': {'token': 4159745}, 'ORIENTBANK': {'token': 636673}, 'MANAPPURAM': {'token': 4879617}, 'TATAELXSI': {'token': 873217}, 'COLPAL': {'token': 3876097}, 'HDFCBANK': {'token': 341249}, 'ITC': {'token': 424961}, 'ASIANPAINT': {'token': 60417}, 'AUROPHARMA': {'token': 70401}, 'PEL': {'token': 617473}, 'BRITANNIA': {'token': 140033}, 'OIL': {'token': 4464129}, 'M&MFIN': {'token': 3400961}, 'APOLLOTYRE': {'token': 41729}, 'SUNPHARMA': {'token': 857857}, 'ENGINERSIN': {'token': 1256193}, 'CEATLTD': {'token': 3905025}, 'DLF': {'token': 3771393}, 'NESTLEIND': {'token': 4598529}, 'CANBK': {'token': 2763265}, 'NATIONALUM': {'token': 1629185}, 'ESCORTS': {'token': 245249}, 'POWERGRID': {'token': 3834113}, 'GODFRYPHLP': {'token': 302337}, 'GODREJCP': {'token': 2585345}, 'ONGC': {'token': 633601}, 'MRF': {'token': 582913}, 'BIOCON': {'token': 2911489}, 'M&M': {'token': 519937}, 'DABUR': {'token': 197633}, 'BHARTIARTL': {'token': 2714625}, 'UNIONBANK': {'token': 2752769}, 'NHPC': {'token': 4454401}, 'VOLTAS': {'token': 951809}, 'BAJFINANCE': {'token': 81153}, 'RELINFRA': {'token': 141569}, 'BAJAJFINSV': {'token': 4268801}, 'VEDL': {'token': 784129}, 'PVR': {'token': 3365633}, 'ACC': {'token': 5633}, 'MGL': {'token': 4488705}, 'BPCL': {'token': 134657}, 'NCC': {'token': 593665}, 'STAR': {'token': 1887745}, 'HINDPETRO': {'token': 359937}, 'HEROMOTOCO': {'token': 345089}, 'UPL': {'token': 2889473}, 'IDBI': {'token': 377857}, 'DRREDDY': {'token': 225537}, 'BANKINDIA': {'token': 1214721}, 'NMDC': {'token': 3924993}, 'HCLTECH': {'token': 1850625}, 'DIVISLAB': {'token': 2800641}, 'L&TFH': {'token': 6386689}, 'CHOLAFIN': {'token': 175361}, 'MCX': {'token': 7982337}, 'IBULHSGFIN': {'token': 7712001}, 'ARVIND': {'token': 49409}, 'COALINDIA': {'token': 5215745}, 'TATASTEEL': {'token': 895745}, 'INDUSINDBK': {'token': 1346049}, 'ADANIENT': {'token': 6401}, 'SBIN': {'token': 779521}, 'VGUARD': {'token': 3932673}, 'BAJAJ-AUTO': {'token': 4267265}, 'MUTHOOTFIN': {'token': 6054401}, 'KSCL': {'token': 3832833}, 'GODREJIND': {'token': 2796801}, 'LUPIN': {'token': 2672641}, 'RAYMOND': {'token': 731905}, 'SHREECEM': {'token': 794369}, 'BATAINDIA': {'token': 94977}, 'KTKBANK': {'token': 2061825}, 'JSWSTEEL': {'token': 3001089}, 'GMRINFRA': {'token': 3463169}, 'TATAGLOBAL': {'token': 878593}, 'HINDUNILVR': {'token': 356865}, 'TORNTPOWER': {'token': 3529217}, 'TATACHEM': {'token': 871681}, 'BERGEPAINT': {'token': 103425}, 'BHARATFIN': {'token': 4995329}, 'SYNDIBANK': {'token': 1837825}, 'LICHSGFIN': {'token': 511233}, 'CENTURYTEX': {'token': 160001}, 'DISHTV': {'token': 3721473}, 'KOTAKBANK': {'token': 492033}, 'JISLJALEQS': {'token': 2661633}, 'INFRATEL': {'token': 7458561}, 'UJJIVAN': {'token': 4369665}, 'TORNTPHARM': {'token': 900609}, 'AMBUJACEM': {'token': 325121}, 'BEL': {'token': 98049}, 'YESBANK': {'token': 3050241}, 'BANKBARODA': {'token': 1195009}, 'NTPC': {'token': 2977281}, 'SRF': {'token': 837889}, 'WOCKPHARMA': {'token': 1921537}, 'BALKRISIND': {'token': 85761}, 'NBCC': {'token': 8042241}, 'INDIACEM': {'token': 387841}, 'APOLLOHOSP': {'token': 40193}, 'HINDZINC': {'token': 364545}, 'CESC': {'token': 160769}, 'FEDERALBNK': {'token': 261889}, 'ADANIPORTS': {'token': 3861249}, 'IGL': {'token': 2883073}, 'ICICIPRULI': {'token': 4774913}, 'INFY': {'token': 408065}, 'CUMMINSIND': {'token': 486657}, 'CGPOWER': {'token': 194561}, 'PNB': {'token': 2730497}, 'JUSTDIAL': {'token': 7670273}, 'OFSS': {'token': 2748929}, 'EQUITAS': {'token': 4314113}, 'SIEMENS': {'token': 806401}, 'MARICO': {'token': 1041153}, 'UBL': {'token': 4278529}, 'PAGEIND': {'token': 3689729}, 'PIDILITIND': {'token': 681985}, 'BSOFT': {'token': 1790465}, 'CANFINHOME': {'token': 149249}, 'PETRONET': {'token': 2905857}, 'ADANIPOWER': {'token': 4451329}, 'HAVELLS': {'token': 2513665}, 'KAJARIACER': {'token': 462849}, 'JETAIRWAYS': {'token': 2997505}}


def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


print("data")

while True:
    for name in trd_portfolio:
        print(name)

        token = trd_portfolio[name]['token']
        from_date = datetime.date(2018, 5, 22)
        to_date = datetime.date(2019, 5, 22)

        main_record = []
        while True:

            try:
                records = kite.historical_data(token, from_date, to_date, interval)
                print(len(records))
            except:
                print("an error occured: try again")
                continue

            #print("got data",trd_portfolio[token])

            for ind in records:
                main_record.append(ind)

            from_date = from_date+tdelta0
            to_date = from_date+tdelta

            break

        kk = json.dumps(main_record, default=myconverter)
        # print(kk)
        open(str(name)+".json", "w+").write(kk)
        # open(str(trd_portfolio[token])+".txt","w+")
    break
