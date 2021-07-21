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
access_token = "2Q8386SojhsgKKVjdNdLFFuJjwdnHJbU"


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

# trd_portfolio = {7455745: "PCJEWELLER", 5633: "ACC", 975873: "ZEEL", 13992450: "BANKNIFTY19AUGFUT"}

trd_portfolio = {121345: {"name": "3MINDIA"}, 3038209: {"name": "63MOONS"}, 1793: {"name": "AARTIIND"}, 2561: {"name": "ABAN"}, 3329: {"name": "ABB"}, 7707649: {"name": "ABFRL"}, 5633: {"name": "ACC"}, 3478273: {"name": "ACE"}, 6401: {"name": "ADANIENT"}, 3861249: {"name": "ADANIPORTS"}, 4451329: {"name": "ADANIPOWER"}, 3350017: {"name": "AIAENG"}, 2079745: {"name": "AJANTPHARM"}, 375553: {"name": "AKZOINDIA"}, 2760193: {"name": "ALBK"}, 2995969: {"name": "ALKEM"}, 3456257: {"name": "ALLCARGO"}, 25601: {"name": "AMARAJABAT"}, 325121: {"name": "AMBUJACEM"}, 3486721: {"name": "ANANTRAJ"}, 40193: {"name": "APOLLOHOSP"}, 41729: {"name": "APOLLOTYRE"}, 49409: {"name": "ARVIND"}, 1376769: {"name": "ASAHIINDIA"}, 54273: {"name": "ASHOKLEY"}, 60417: {"name": "ASIANPAINT"}, 1436161: {"name": "ASTRAZEN"}, 425729: {"name": "ATFL"}, 67329: {"name": "ATUL"}, 5436929: {"name": "AUBANK"}, 70401: {"name": "AUROPHARMA"}, 71169: {"name": "AUTOAXLES"}, 2031617: {"name": "AVANTIFEED"}, 1510401: {"name": "AXISBANK"}, 4267265: {"name": "BAJAJ-AUTO"}, 3848705: {"name": "BAJAJELEC"}, 4268801: {"name": "BAJAJFINSV"}, 78081: {"name": "BAJAJHLDNG"}, 81153: {"name": "BAJFINANCE"}, 85761: {"name": "BALKRISIND"}, 87297: {"name": "BALRAMCHIN"}, 3553281: {"name": "BANCOINDIA"}, 1195009: {"name": "BANKBARODA"}, 2928385: {"name": "BANKBEES"}, 1214721: {"name": "BANKINDIA"}, 94977: {"name": "BATAINDIA"}, 97281: {"name": "BBTC"}, 98049: {"name": "BEL"}, 101121: {"name": "BEML"}, 103425: {"name": "BERGEPAINT"}, 3729153: {"name": "BFUTILITIE"}, 4995329: {"name": "BHARATFIN"}, 108033: {"name": "BHARATFORG"}, 2714625: {"name": "BHARTIARTL"}, 112129: {"name": "BHEL"}, 2911489: {"name": "BIOCON"}, 4931841: {"name": "BLISSGVS"}, 3402241: {"name": "BLKASHYAP"}, 126721: {"name": "BLUEDART"}, 558337: {"name": "BOSCHLTD"}, 134657: {"name": "BPCL"}, 140033: {"name": "BRITANNIA"}, 501376: {"name": "BSE"}, 2029825: {"name": "CADILAHC"}, 1591297: {"name": "CAMLINFINE"}, 2763265: {"name": "CANBK"}, 149249: {"name": "CANFINHOME"}, 5567745: {"name": "CAPACITE"}, 320001: {"name": "CASTROLIND"}, 5420545: {"name": "CDSL"}, 3905025: {"name": "CEATLTD"}, 628225: {"name": "CENTRUM"}, 3406081: {"name": "CENTURYPLY"}, 160001: {"name": "CENTURYTEX"}, 7683073: {"name": "CEREBRAINT"}, 160769: {"name": "CESC"}, 5204225: {"name": "CGCL"}, 194561: {"name": "CGPOWER"}, 524545: {"name": "CHENNPETRO"}, 175361: {"name": "CHOLAFIN"}, 177665: {"name": "CIPLA"}, 8151809: {"name": "CNOVAPETRO"}, 5215745: {"name": "COALINDIA"}, 5506049: {"name": "COCHINSHIP"}, 2858241: {"name": "COFFEEDAY"}, 3876097: {"name": "COLPAL"}, 1215745: {"name": "CONCOR"}, 189185: {"name": "COROMANDEL"}, 4558337: {"name": "COX&KINGS"}, 193793: {"name": "CRISIL"}, 4376065: {"name": "CROMPTON"}, 1459457: {"name": "CUB"}, 486657: {"name": "CUMMINSIND"}, 1471489: {"name": "CYIENT"}, 3536897: {"name": "DAAWAT"}, 197633: {"name": "DABUR"}, 199937: {"name": "DALMIASUG"}, 4577537: {"name": "DBCORP"}, 4630017: {"name": "DBL"}, 3513601: {"name": "DCBBANK"}, 207617: {"name": "DCMSHRIRAM"}, 3851265: {"name": "DELTACORP"}, 4536833: {"name": "DEN"}, 219393: {"name": "DHAMPURSUG"}, 215553: {"name": "DHFL"}, 5591041: {"name": "DIAMONDYD"}, 3721473: {"name": "DISHTV"}, 2800641: {"name": "DIVISLAB"}, 5552641: {"name": "DIXON"}, 3771393: {"name": "DLF"}, 5097729: {"name": "DMART"}, 3501569: {"name": "DOLPHINOFF"}, 2885377: {"name": "DREDGECORP"}, 225537: {"name": "DRREDDY"}, 3885825: {"name": "ECLERX"}, 232961: {"name": "EICHERMOT"}, 234497: {"name": "EIDPARRY"}, 235265: {"name": "EIHOTEL"}, 237569: {"name": "ELECTCAST"}, 3460353: {"name": "EMAMILTD"}, 4818433: {"name": "ENDURANCE"}, 1256193: {"name": "ENGINERSIN"}, 4314113: {"name": "EQUITAS"}, 5415425: {"name": "ERIS"}, 5140481: {"name": "EROSMEDIA"}, 245249: {"name": "ESCORTS"}, 6211841: {"name": "ESTER"}, 3016193: {"name": "EVEREADY"}, 173057: {"name": "EXIDEIND"}, 261889: {"name": "FEDERALBNK"}, 2692097: {"name": "FEL"}, 265729: {"name": "FINCABLES"}, 3735553: {"name": "FORTIS"}, 4704769: {"name": "FRETAIL"}, 1207553: {"name": "GAIL"}, 1777665: {"name": "GANECOS"}, 3504129: {"name": "GATI"}, 3004161: {"name": "GDL"}, 2012673: {"name": "GEPIL"}, 3526657: {"name": "GESHIP"}, 4296449: {"name": "GET&D"}, 288513: {"name": "GHCL"}, 291585: {"name": "GICHSGFIN"}, 70913: {"name": "GICRE"}, 403457: {"name": "GILLETTE"}, 295169: {"name": "GLAXO"}, 1895937: {"name": "GLENMARK"}, 4460545: {"name": "GLOBUSSPR"}, 299009: {"name": "GMBREW"}, 3463169: {"name": "GMRINFRA"}, 4754177: {"name": "GNA"}, 300545: {"name": "GNFC"}, 302337: {"name": "GODFRYPHLP"}, 36865: {"name": "GODREJAGRO"}, 2585345: {"name": "GODREJCP"}, 2796801: {"name": "GODREJIND"}, 4576001: {"name": "GODREJPROP"}, 3693569: {"name": "GOLDBEES"}, 5051137: {"name": "GPPL"}, 3039233: {"name": "GRANULES"}, 315393: {"name": "GRASIM"}, 316161: {"name": "GREAVESCOT"}, 319233: {"name": "GSFC"}, 821761: {"name": "GSKCONS"}, 3378433: {"name": "GSPL"}, 3928833: {"name": "GSS"}, 324353: {"name": "GUJALKALI"}, 329985: {"name": "GUJFLUORO"}, 2713345: {"name": "GUJGASLTD"}, 4647425: {"name": "HATHWAY"}, 2513665: {"name": "HAVELLS"}, 3575297: {"name": "HBLPOWER"}, 339713: {"name": "HCL-INSYS"}, 1850625: {"name": "HCLTECH"}, 340481: {"name": "HDFC"}, 1086465: {"name": "HDFCAMC"}, 341249: {"name": "HDFCBANK"}, 119553: {"name": "HDFCLIFE"}, 592897: {"name": "HEIDELBERG"}, 345089: {"name": "HEROMOTOCO"}, 2747905: {"name": "HEXAWARE"}, 3766273: {"name": "HGS"}, 2475009: {"name": "HIKAL"}, 348929: {"name": "HINDALCO"}, 4592385: {"name": "HINDCOPPER"}, 359937: {"name": "HINDPETRO"}, 356865: {"name": "HINDUNILVR"}, 364545: {"name": "HINDZINC"}, 874753: {"name": "HONAUT"}, 3669505: {"name": "HSCL"}, 361473: {"name": "HSIL"}, 5331201: {"name": "HUDCO"}, 7712001: {"name": "IBULHSGFIN"}, 1270529: {"name": "ICICIBANK"}, 5573121: {"name": "ICICIGI"}, 7565569: {"name": "ICICINIFTY"}, 4774913: {"name": "ICICIPRULI"}, 377857: {"name": "IDBI"}, 3677697: {"name": "IDEA"}, 3060993: {"name": "IDFC"}, 2863105: {"name": "IDFCFIRSTB"}, 56321: {"name": "IEX"}, 381697: {"name": "IFCI"}, 2883073: {"name": "IGL"}, 387073: {"name": "INDHOTEL"}, 387841: {"name": "INDIACEM"}, 3663105: {"name": "INDIANB"}, 2865921: {"name": "INDIGO"}, 1346049: {"name": "INDUSINDBK"}, 4159745: {"name": "INFIBEAM"}, 7458561: {"name": "INFRATEL"}, 408065: {"name": "INFY"}, 3384577: {"name": "INOXLEISUR"}, 2010113: {"name": "INOXWIND"}, 1517057: {"name": "INTELLECT"}, 2393089: {"name": "IOB"}, 415745: {"name": "IOC"}, 418049: {"name": "IPCALAB"}, 3920129: {"name": "IRB"}, 424961: {"name": "ITC"}, 1439233: {"name": "ITDCEM"}, 3382017: {"name": "JAGRAN"}, 1316609: {"name": "JAICORPLTD"}, 5319169: {"name": "JAMNAAUTO"}, 1034497: {"name": "JAYAGROGN"}, 440321: {"name": "JAYSREETEA"}, 2997505: {"name": "JETAIRWAYS"}, 1723649: {"name": "JINDALSTEL"}, 5284353: {"name": "JINDWORLD"}, 2661633: {"name": "JISLJALEQS"}, 3397121: {"name": "JKCEMENT"}, 3036161: {"name": "JKPAPER"}, 3695361: {"name": "JKTYRE"}, 3491073: {"name": "JMFINANCIL"}, 2933761: {"name": "JPASSOCIAT"}, 3149825: {"name": "JSLHISAR"}, 4574465: {"name": "JSWENERGY"}, 3001089: {"name": "JSWSTEEL"}, 931073: {"name": "JUBILANT"}, 4632577: {"name": "JUBLFOOD"}, 7670273: {"name": "JUSTDIAL"}, 3877377: {"name": "JYOTHYLAB"}, 462849: {"name": "KAJARIACER"}, 464385: {"name": "KALPATPOWR"}, 306177: {"name": "KANSAINER"}, 470529: {"name": "KARURVYSYA"}, 3394561: {"name": "KEC"}, 3407361: {"name": "KEI"}, 108801: {"name": "KHADIM"}, 5103873: {"name": "KILITCH"}, 4259585: {"name": "KIRIINDUS"}, 492033: {"name": "KOTAKBANK"}, 4634113: {"name": "KOTAKNIFTY"}, 3832833: {"name": "KSCL"}, 2061825: {"name": "KTKBANK"}, 6386689: {"name": "L&TFH"}, 2983425: {"name": "LALPATHLAB"}, 510465: {"name": "LIBERTSHOE"}, 511233: {"name": "LICHSGFIN"}, 2968577: {"name": "LINCOLN"}, 2817537: {"name": "LIQUIDBEES"}, 5738241: {"name": "LOVABLE"}, 2939649: {"name": "LT"}, 2672641: {"name": "LUPIN"}, 519937: {"name": "M&M"}, 3400961: {"name": "M&MFIN"}, 4937985: {"name": "M50"}, 2919169: {"name": "MAGMA"}, 3823873: {"name": "MAHINDCIE"}, 98561: {"name": "MAHLOG"}, 534529: {"name": "MAHSEAMLES"}, 2639361: {"name": "MAJESCO"}, 3531777: {"name": "MANALIPETC"}, 4879617: {"name": "MANAPPURAM"}, 539905: {"name": "MANGTIMBER"}, 3042305: {"name": "MANINDS"}, 4665857: {"name": "MANINFRA"}, 1041153: {"name": "MARICO"}, 2708225: {"name": "MARKSANS"}, 2815745: {"name": "MARUTI"}, 50945: {"name": "MASFIN"}, 543745: {"name": "MASTEK"}, 5561857: {"name": "MATRIMONY"}, 2674433: {"name": "MCDOWELL-N"}, 3057409: {"name": "MCLEODRUSS"}, 7982337: {"name": "MCX"}, 3776001: {"name": "MEGH"}, 548353: {"name": "MFSL"}, 4488705: {"name": "MGL"}, 630529: {"name": "MIDHANI"}, 6629633: {"name": "MINDACORP"}, 3623425: {"name": "MINDAIND"}, 3675137: {"name": "MINDTREE"}, 4596993: {"name": "MMTC"}, 5332481: {"name": "MOIL"}, 1718529: {"name": "MOLDTKPAC"}, 578305: {"name": "MOREPENLAB"}, 1076225: {"name": "MOTHERSUMI"}, 1152769: {"name": "MPHASIS"}, 582913: {"name": "MRF"}, 584449: {"name": "MRPL"}, 2899201: {"name": "MUKANDLTD"}, 3458817: {"name": "MUNJALAU"}, 6054401: {"name": "MUTHOOTFIN"}, 1003009: {"name": "NATCOPHARM"}, 1629185: {"name": "NATIONALUM"}, 3520257: {"name": "NAUKRI"}, 3756033: {"name": "NAVINFLUOR"}, 610561: {"name": "NAVNETEDUL"}, 8042241: {"name": "NBCC"}, 593665: {"name": "NCC"}, 4598529: {"name": "NESTLEIND"}, 3612417: {"name": "NETWORK18"}, 3564801: {"name": "NFL"}, 3031041: {"name": "NH"}, 4454401: {"name": "NHPC"}, 102145: {"name": "NIACL"}, 2707457: {"name": "NIFTYBEES"}, 2949633: {"name": "NIITLTD"}, 2955009: {"name": "NIITTECH"}, 2197761: {"name": "NLCINDIA"}, 3924993: {"name": "NMDC"}, 625153: {"name": "NOCIL"}, 1933569: {"name": "NRBBEARING"}, 2977281: {"name": "NTPC"}, 5181953: {"name": "OBEROIRLTY"}, 2748929: {"name": "OFSS"}, 4464129: {"name": "OIL"}, 3802369: {"name": "OMAXE"}, 633601: {"name": "ONGC"}, 636673: {"name": "ORIENTBANK"}, 7702785: {"name": "ORIENTCEM"}, 3689729: {"name": "PAGEIND"}, 655873: {"name": "PAPERPROD"}, 4385281: {"name": "PARAGMILK"}, 2994945: {"name": "PATELENG"}, 7455745: {"name": "PCJEWELLER"}, 617473: {"name": "PEL"}, 4701441: {"name": "PERSISTENT"}, 2905857: {"name": "PETRONET"}, 3660545: {"name": "PFC"}, 676609: {"name": "PFIZER"}, 648961: {"name": "PGHH"}, 678145: {"name": "PHILIPCARB"}, 3725313: {"name": "PHOENIXLTD"}, 681985: {"name": "PIDILITIND"}, 6191105: {"name": "PIIND"}, 2730497: {"name": "PNB"}, 2236417: {"name": "PNBGILTS"}, 4840449: {"name": "PNBHOUSING"}, 687873: {"name": "POLYPLEX"}, 3834113: {"name": "POWERGRID"}, 692481: {"name": "PRAJIND"}, 5197313: {"name": "PRESTIGE"}, 2906881: {"name": "PTC"}, 3820033: {"name": "PURVA"}, 3365633: {"name": "PVR"}, 3357697: {"name": "QUICKHEAL"}, 2813441: {"name": "RADICO"}, 5088513: {"name": "RADIOCITY"}, 1894657: {"name": "RAJESHEXPO"}, 720897: {"name": "RALLIS"}, 523009: {"name": "RAMCOCEM"}, 1174273: {"name": "RAMCOIND"}, 5154305: {"name": "RAMKY"}, 731905: {"name": "RAYMOND"}, 4708097: {"name": "RBLBANK"}, 733697: {"name": "RCF"}, 3930881: {"name": "RECLTD"}, 6201601: {"name": "RELAXO"}, 737793: {"name": "RELCAPITAL"}, 738561: {"name": "RELIANCE"}, 141569: {"name": "RELINFRA"}, 7577089: {"name": "REPCOHOME"}, 744705: {"name": "RICOAUTO"}, 745473: {"name": "RIIL"}, 2921217: {"name": "RKFORGE"}, 3906305: {"name": "RPOWER"}, 3388417: {"name": "SADBHAV"}, 758529: {"name": "SAIL"}, 3392257: {"name": "SAKUMA"}, 5468673: {"name": "SALASAR"}, 2918145: {"name": "SALZERELEC"}, 767233: {"name": "SANGHIIND"}, 3598849: {"name": "SANGHVIMOV"}, 369153: {"name": "SANOFI"}, 1252353: {"name": "SAREGAMA"}, 2675969: {"name": "SATIN"}, 5582849: {"name": "SBILIFE"}, 779521: {"name": "SBIN"}, 258817: {"name": "SCHAEFFLER"}, 5298689: {"name": "SCHAND"}, 7995905: {"name": "SCHNEIDER"}, 780289: {"name": "SCI"}, 3481089: {"name": "SELAN"}, 3659777: {"name": "SEQUENT"}, 2695681: {"name": "SHARDAMOTR"}, 794369: {"name": "SHREECEM"}, 3005185: {"name": "SHRIRAMCIT"}, 806401: {"name": "SIEMENS"}, 809473: {"name": "SIMPLEXINF"}, 1492737: {"name": "SINTEX"}, 5504257: {"name": "SIS"}, 4834049: {"name": "SJVN"}, 815617: {"name": "SKFINDIA"}, 1239809: {"name": "SNOWMAN"}, 3539457: {"name": "SOBHA"}, 3412993: {"name": "SOLARINDS"}, 1522689: {"name": "SOUTHBANK"}, 3785729: {"name": "SPARC"}, 5494273: {"name": "SPTL"}, 836353: {"name": "SREINFRA"}, 837889: {"name": "SRF"}, 1102337: {"name": "SRTRANSFIN"}, 1887745: {"name": "STAR"}, 2802689: {"name": "STCINDIA"}, 2383105: {"name": "STRTECH"}, 854785: {"name": "SUNDARMFIN"}, 856321: {"name": "SUNDRMFAST"}, 857857: {"name": "SUNPHARMA"}, 4516097: {"name": "SUNTECK"}, 3431425: {"name": "SUNTV"}, 860929: {"name": "SUPREMEIND"}, 2875649: {"name": "SUVEN"}, 3076609: {"name": "SUZLON"}, 1837825: {"name": "SYNDIBANK"}, 2622209: {"name": "SYNGENE"}, 3818753: {"name": "TAKE"}, 4812033: {"name": "TALWALKARS"}, 3577857: {"name": "TANLA"}, 871681: {"name": "TATACHEM"}, 185345: {"name": "TATACOFFEE"}, 952577: {"name": "TATACOMM"}, 873217: {"name": "TATAELXSI"}, 878593: {"name": "TATAGLOBAL"}, 414977: {"name": "TATAINVEST"}, 884737: {"name": "TATAMOTORS"}, 4343041: {"name": "TATAMTRDVR"}, 877057: {"name": "TATAPOWER"}, 419585: {"name": "TATASPONGE"}, 895745: {"name": "TATASTEEL"}, 6921473: {"name": "TBZ"}, 2708481: {"name": "TCI"}, 2953217: {"name": "TCS"}, 3465729: {"name": "TECHM"}, 5409537: {"name": "TEJASNET"}, 4662785: {"name": "TEXMOPIPES"}, 5587969: {"name": "TEXRAIL"}, 889601: {"name": "THERMAX"}, 891137: {"name": "THOMASCOOK"}, 4360193: {"name": "THYROCARE"}, 5565441: {"name": "TIFIN"}, 3764993: {"name": "TIMETECHNO"}, 894209: {"name": "TINPLATE"}, 897537: {"name": "TITAN"}, 898305: {"name": "TNPETRO"}, 1018881: {"name": "TNPL"}, 900609: {"name": "TORNTPHARM"}, 3529217: {"name": "TORNTPOWER"}, 502785: {"name": "TRENT"}, 2479361: {"name": "TRIDENT"}, 1389569: {"name": "TRIGYN"}, 3348737: {"name": "TRIVENI"}, 907777: {"name": "TTKPRESTIG"}, 3637249: {"name": "TV18BRDCST"}, 2170625: {"name": "TVSMOTOR"}, 3945985: {"name": "TWL"}, 4278529: {"name": "UBL"}, 2873089: {"name": "UCOBANK"}, 4369665: {"name": "UJJIVAN"}, 2952193: {"name": "ULTRACEMCO"}, 2752769: {"name": "UNIONBANK"}, 923393: {"name": "UNIVCABLES"}, 2889473: {"name": "UPL"}, 2263041: {"name": "USHAMART"}, 784129: {"name": "VEDL"}, 3932673: {"name": "VGUARD"}, 2426625: {"name": "VIJAYABANK"}, 3799809: {"name": "VIPCLOTHNG"}, 947969: {"name": "VIPIND"}, 951809: {"name": "VOLTAS"}, 530689: {"name": "VTL"}, 4330241: {"name": "WABCOINDIA"}, 956417: {"name": "WALCHANNAG"}, 3026177: {"name": "WELCORP"}, 2976257: {"name": "WELENT"}, 2880769: {"name": "WELSPUNIND"}, 4610817: {"name": "WHIRLPOOL"}, 6392065: {"name": "WINDMACHIN"}, 969473: {"name": "WIPRO"}, 1921537: {"name": "WOCKPHARMA"}, 768513: {"name": "WONDERLA"}, 3050241: {"name": "YESBANK"}, 975873: {"name": "ZEEL"}}


def on_ticks(ws, ticks):

    # pdb.set_trace()
    print("\n", "new loop")
    for sc in ticks:
        token = sc['instrument_token']
        name = trd_portfolio[token]['name']
        specs = trd_portfolio[token]
        openx = sc['ohlc']['open']
        high = sc['ohlc']['high']
        low = sc['ohlc']['low']
        close = sc['ohlc']['close']

        # print("\n", name, openx, high, low, close)

        if openx == low and 'status' not in specs.keys():
            print(f"buy {name}")
            specs['status'] = "buy"
            # pdb.set_trace()

        if openx == high and 'status' not in specs.keys():
            print(f"sell {name}")
            specs['status'] = "sell"

        # pdb.set_trace()

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


inst_token = [x for x in trd_portfolio]


def on_connect(ws, response):
    ws.subscribe(inst_token)
    ws.set_mode(ws.MODE_FULL, inst_token)


kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.connect()
ct
kws.connect()
t()
