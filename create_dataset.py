import billboard
import csv
import pylast
from datetime import datetime
import pickle

a = dict()  # "Title" : "Artist", "User1" ..... "User2000", "Hit i.e. peak position <= 20 in future"

def timeconv(time):
    a = time.split('-')
    dt = datetime(int(a[0]), int(a[1]), int(a[2]))
    timestamp = (dt - datetime(1970, 1, 1)).total_seconds()
    return str(int(timestamp))

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from https://www.last.fm/api/account/create for Last.fm
API_KEY = ""
API_SECRET = ""

# In order to perform a write operation you need to authenticate yourself
username = "nikhilranjan"
password_hash = pylast.md5("")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)

chart = billboard.ChartData('hot-100')

while int(chart.date[:4])>2010:
    print("going_through",chart.date)
    for i in range(100):
        if chart[i].title not in a:
            a[chart[i].title] = [0] * 2000
            a[chart[i].title].insert(0,chart[i].artist)
            if(chart[i].peakPos <= 20):
                a[chart[i].title] += [1]
            else:
                a[chart[i].title] += [0]
    chart = billboard.ChartData('hot-100', chart.previousDate)

with open('dataset', 'wb') as f:
    pickle.dump(a,f)
