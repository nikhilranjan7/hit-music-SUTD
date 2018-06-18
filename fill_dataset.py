from users import userlist1
from date import date
import pickle

count = 0
with open('songs', 'rb') as f:
    songs = pickle.load(f)

with open('dataset', 'rb') as f:
    dataset = pickle.load(f)

files = ['file' + str(i) for i in range(1,21)]

for m in range(len(files)):
    count = 0
    with open('Download/'+files[m], 'rb') as f:
        usergroup = pickle.load(f)

    for song in dataset:
        print("Progress:",(count/len(dataset))*100, "%", "&",m,"iterations out of 20")
        count += 1
        s = song.lower()
        flag = False
        for i in songs[s][::-1]:
            if i[1] > 20:
                for j in usergroup:
                    try:
                        if(s in j[date.index(i[0])]):
                            print("\n\n\n***MATCH***\n\n\n")
                            dataset[song][(m*100)+usergroup.index(j)+1] = 1
                    except Exception as e:
                        pass

with open('dataset', 'wb') as f:
    pickle.dump(dataset,f)
