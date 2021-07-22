from datetime import date, timedelta

def allthursday(year):
   d = date(year, 1, 1)                    # January 1st
   d += timedelta(days = 10 - d.weekday()) # First Thursday

   while d.year == year:
      yield d
      d += timedelta(days = 7)


def nextThursday(year):
    dates =[]
    dates1 = []
    for d in allthursday(year):
        if date.today()< d:
            if 10 > int(str(d).split('-')[1]):
                dates.append(str(d))
            elif(10 < int(str(d).split('-')[1]) and int(str(d).split('-')[2]) < 25):
                lst = {10:'O', 11:'N', 12:'D'}
                mt = int(str(d).split('-')[1])
                yy = str(d).split('-')[0]
                dd = str(d).split('-')[2]
                d = yy+"-"+lst[mt]+"-"+dd
                dates.append(str(d))
            else:
                dates.append(str(d))

    for dd in dates:
        dd1 = str(dd).split('-')[2]
        if int(dd1) >= 25:
            lst1 = {1:'JAN', 2:'FEB', 3:'MAR', 4:'APR', 5:'MAY',
                    6:'JUN', 7:'JUL', 8:'AUG', 9:'SEP',
                    10:'OCT', 11:'NOV', 12:'DEC'
                }
            mt1 = int(str(dd).split('-')[1])
            yy1 = str(dd).split('-')[0]
            dd11 = str(dd).split('-')[2]
            d1 = yy1+"-"+lst1[mt1]+"-"+dd11
            dates1.append(d1)
        else:
            dates1.append(dd)

    return dates1


#print(nextThursday(2021))

#   NSE:BANKNIFTY20N0525000PE

# NSE:BANKNIFTY21JUL35000CE
# NSE:BANKNIFTY21JUL2935200CE