import billboard
from date import date
import pickle

with open('dataset', 'rb') as f:
    x = pickle.load(f)

songs = dict()

for i in x:
    songs[i.lower()] = []

for d in date:
    print("Completed",date.index(d)/len(date),"%")
    chart = billboard.ChartData('hot-100', date=d)
    for i in range(100):
        songs[chart[i].title.lower()].append([d, chart[i].rank, chart[i].isNew])


with open('songs', 'wb') as f:
    pickle.dump(songs,f)
