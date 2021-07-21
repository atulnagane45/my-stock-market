import time
import datetime
# Date comparision

value = datetime.datetime.now()
# normal time
# print(value)

# strftime
# print(value.strftime("%x"))

# only date
# print(value.date())

# only date
# print(value.time())

# only time-delta
# print(value.date() + datetime.timedelta(days=1))

# today date
# print(datetime.date.today())


# execution speed
start = time.time()
print("some code")
time.sleep(1)

end = time.time()

print(end-start)
