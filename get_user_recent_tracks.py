import billboard
import csv
import pylast
from datetime import datetime
from users import userlist

data = [0]*2000

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
date = []
while int(chart.date[:4])>2010:
    date.append(chart.date)
    print("Still filling the date",chart.date)
    chart = billboard.ChartData('hot-100', chart.previousDate)

for i in range(len(userlist)):
    for j in range(len(date)):
        print("Doing for user", i+1, "and date", date[j])
        data[i] = [0]*len(date)
        try:
            user = network.get_user(userlist[j])
            t = user.get_recent_tracks(limit=100, time_to=timeconv(date[j]))
        except:
            print("Username not found = ",userlist[j])
            continue
        user_tracks = []
        for k in t:
            user_tracks.append(k.track.title.lower())
        data[i][j] = user_tracks

with open('file.txt', 'w') as f:
    f.write(data)
