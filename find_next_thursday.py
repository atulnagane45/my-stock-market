from datetime import date, timedelta

def allthursday(year):
   d = date(year, 1, 1)                    # January 1st
   d += timedelta(days = 10 - d.weekday()) # First Thursday

   while d.year == year:
      yield d
      d += timedelta(days = 7)


def nextThursday(year):
    dates =[]
    for d in allthursday(year):
        #print(d)
        if date.today()< d:
            dates.append(str(d))

    return dates


print(nextThursday(2021))


#   NSE:BANKNIFTY20N0525000PE