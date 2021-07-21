list

name = ['imran', 'anil', 'manoj']
name[0]
..imran


dictionary:
name = {'imran': 25, 'anil': 35, 'manoj': 10}
name['imran']  # to get value> dictnary_name[key]
..25


nested structure:

{'averaign_cipla': [50, 60, 70], 'averaign_zeel': [500, 560, 580]}


name = {'imran': [20, 21, 22, 23, 24],
	   'anil': {'axisbank': 500, 'cipla': 1000, 'zeel': 50},
	   'manoj': {'averaign_cipla': [50, 60, 70], 'averaign_zeel': [500, 560, 580]}
	   'priya': [{'10': 'cbse'}, {'12': mb}, {'now': 'jobsearch'}]



_________________________________
name['priya']
..[{'10': 'cbse'}, {'12': mb}, {'now': 'jobsearch'}]

name['priya'][2]
..{'now': 'jobsearch'}

name['priya'][2]['now']
'jobsearch'
_________________________________

_________________________________
name['imran']
..[20, 21, 22, 23, 24]

name['imran'][3]
..23
_________________________________



_________________________________
name['anil']
..{'axisbank': 500, 'cipla': 1000, 'zeel': 50}

name['anil']['cipla']
..1000
_________________________________


_________________________________
name['manoj']..
..{'averaign_cipla': [50, 60, 70], 'averaign_zeel': [500, 560, 580]}

name['manoj']['averaign_zeel']
..[500, 560, 580]

name['manoj']['averaign_zeel'][2]

_________________________________
