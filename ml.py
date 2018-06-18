import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
import pickle

df = pd.read_csv('data.csv')

df.head()
u = ['u'+str(i) for i in range(1,2001)]
u += ['hit']
u.insert(0,'artist')
u.insert(0,'title')
df.columns = u
df.head()
df.drop(['title', 'artist'], 1, inplace=True)
df.head()

np_scaled = preprocessing.MinMaxScaler().fit_transform(df)
df_normalized = pd.DataFrame(np_scaled, columns=df.columns, index=df.index)
df_normalized = shuffle(df_normalized)

print("Size:",len(df.index))
df_normalized.head()

train, test = train_test_split(df_normalized, test_size=0.2)
print("Training Size =",train.size,"&","Testing Size =",test.size)
x = train[train.columns.drop('hit')]
y = train['hit']
'''
test = test.transpose()
shuffle(test)
test = test.transpose()
'''
x_test = test[test.columns.drop('hit')]
y_test = test['hit']

from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

names = ["Nearest Neighbors", "Linear SVM", "RBF SVM",
         "Decision Tree", "Random Forest", "Neural Net", "AdaBoost"]

classifiers = [
    KNeighborsClassifier(3,  n_jobs = -1),
    SVC(kernel="linear", C=0.025),
    SVC(gamma=2, C=1),
    #GaussianProcessClassifier(1.0 * RBF(1.0),  n_jobs = -1),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10,
                           max_features=1),
    MLPClassifier(alpha=1),
    AdaBoostClassifier()]

result = []
model = []
for name, clf in zip(names, classifiers):
        print("Running:",name)
        clf.fit(x, y)
        score = clf.score(x_test, y_test)
        model.append(clf)
        result.append([name, score])

result_final = pd.DataFrame(result, columns=['Classifier', 'Score'])
print(result_final)


filename = 'trained_model'
pickle.dump(model, open(filename, 'wb'))

'''
filename = 'trained_model'
model = pickle.load(open(filename, 'rb'))

df = pd.read_csv('data.csv')

while(1):
    s = input("Write the name of the song to predict: ")
    ans = []
    s = list(df[df.columns[0]].values).index(s)
    d = df.values[s]
    d = d[2:]
    d = d[:-1]
    d = d.reshape(1, -1)
    for e in model:
        ans.append(int(e.predict(d)[0]))

    print(ans)
    print("The song will be",max(set(ans), key = ans.count))

random = ['#SELFIE', 'i', 'iSpy', 'God\'s Plan', '#thatPOWER']
'''
