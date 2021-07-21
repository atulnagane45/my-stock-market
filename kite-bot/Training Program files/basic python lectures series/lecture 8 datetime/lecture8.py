import datetime

breakout_time = datetime.time(9, 30)

current_time = datetime.datetime.now().time()
# print(breakout_time, current_time)

if current_time > breakout_time:
    print("i am starting code")
