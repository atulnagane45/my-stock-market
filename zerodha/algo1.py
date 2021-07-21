import yaml
import time, sys
import datetime
from playsound import playsound

###################################################
with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

def nowtime():
    return datetime.datetime.now()

######################################
playsound('./sound/comp.wav')
button = cfg['button'] #on/off
mytime = cfg['time']

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

if button:
    print("trading is on today ...")
    while button:
        print(nowtime())
        if nowtime() > tradtime1 and nowtime() < tradstoptime1:
            print('order placed')
            playsound('./sound/place.wav')
            break;
            #sys.exit()

        time.sleep(5)
          



    #order exit loop call
    print("next call")

        



else:
    print("No tread today ...")