import pandas as pd
import pickle

df = pd.read_csv('data.csv')
with open('trained_model', 'rb') as f:
    model = pickle.load(open('trained_model', 'rb'))


a = list(df[df.columns[0]].values)
count = 0
for i in a:
    count += 1
    s = i
    ans = []
    s = list(df[df.columns[0]].values).index(s)
    d = df.values[s]
    d = d[2:]
    d = d[:-1]
    d = d.reshape(1, -1)

    for e in model:
        ans.append(str(int(e.predict(d)[0])))
    names = ["Nearest_Neighbors", "Linear_SVM", "RBF_SVM", "Decision_Tree", "Random_Forest", "Neural_Net", "AdaBoost"]
    context_dict = dict()
    context_dict['hit'] = str(max(set(ans), key = ans.count))
    ans.append(context_dict['hit'])
    ans = "".join(ans)
    print('   { value: "%s" , data: "%s"  },'%(i,ans))
