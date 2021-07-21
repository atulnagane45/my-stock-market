"""
from nse import Nse

db = Nse()

data = db.live("HDFCBANK")   
print(data)
"""
from pprint import pprint
from nse import Nse
db = Nse()
"""
#Historical Data
Hdata = db.history("HDFCBANK","01-01-2020",'25-11-2020')
pprint(Hdata)

"""

# Capture HDFCBANK Live Data For 5 Minutes
db.capture(['HDFCBANK'],1)   
#Load Captured Data Of HDFCBANK
data = db.load('HDFCBANK')
pprint(data)


