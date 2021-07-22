import yaml
import time, sys
import datetime
from playsound import playsound
from find_next_thursday import nextThursday
from order import optionBuyOrder, optionSellOrder

###################################################
with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

def nowtime():
    return datetime.datetime.now()
def year():
    return str(datetime.datetime.now().year)

######################################
playsound('./sound/comp.wav')
button = cfg['button'] #on/off
mytime = cfg['time']

yy = year()[-2:]
now = nowtime()
hour = int(mytime.split(':')[0])
minute = int(mytime.split(':')[1])

tradtime1 = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
tradstoptime1 = now.replace(hour=hour, minute=minute+1, second=0, microsecond=0)
orders = []

#################
print('button status =', button)
print('current date time = ', nowtime())
print('my tradtime1 =', tradtime1)

symbol = "BANKNIFTY"
current_strike = 34800
print("symbol = ", symbol, current_strike)

def createCurrentWeekStrike(symbol, strike, opt_Type):
    next_thu = nextThursday(int(year()))[0]
    try:
        date = str((next_thu.split('-'))[2])
        month = str((next_thu.split('-'))[1])[-1:]
        mm = int(month)
    except:
        month = str((next_thu.split('-'))[1])
        return "NSE:"+symbol + yy + month + strike+ opt_Type

    return "NSE:"+symbol + yy + month + date + strike+ opt_Type

def createNextWeekStrike(symbol, strike, opt_Type):
    next_thu = nextThursday(int(year()))[1]
    try:
        date = str((next_thu.split('-'))[2])
        month = str((next_thu.split('-'))[1])[-1:]
        mm = int(month)
    except:
        month = str((next_thu.split('-'))[1])
        return "NSE:"+symbol + yy + month + strike+ opt_Type
    return "NSE:"+symbol + yy + month + date + strike+ opt_Type


if button:
    print("trading is on today ...")
    while button:
        print(nowtime())
        if nowtime() > tradtime1 and nowtime() < tradstoptime1:
            print('order placed')
            s1 = createNextWeekStrike(symbol, str(current_strike +200), "CE")
            print("option name =",s1)
            order1 = optionSellOrder(s1)
            print(order1)
            s2 = createNextWeekStrike(symbol, str(current_strike -200), "PE")
            print("option name =",s2)
            order2 = optionSellOrder(s2)
            print(order2)

            playsound('./sound/place.wav')
            break;
            #sys.exit()

        time.sleep(5)
          



    #order exit loop call
    print("next call")

        



else:
    print("No tread today ...")