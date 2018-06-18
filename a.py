#{ value: 'Afghan afghani', data: 'AFN' },

import pandas as pd

df = pd.read_csv('data.csv')

a = list(df[df.columns[0]].values
with open('static/trained_model', 'rb') as f:
    model = pickle.load(f)

for i in a:
    s = i
    ans = []
    s = list(df[df.columns[0]].values).index(s)
    d = df.values[s]
    d = d[2:]
    d = d[:-1]
    d = d.reshape(1, -1)

    for e in model:
        ans.append(int(e.predict(d)[0]))
    names = ["Nearest_Neighbors", "Linear_SVM", "RBF_SVM", "Decision_Tree", "Random_Forest", "Neural_Net", "AdaBoost"]
    for i in range(len(names)):
        context_dict[names[i]] = ans[i]
    context_dict['hit'] = max(set(ans), key = ans.count)

    print("   { value: %s , Nearest_Neighbors: %d, Linear_SVM: %d, RBF_SVM: %d, Decision_Tree: %d, Random_Forest: %d, Neural_Net: %d, AdaBoost: %d  }"%(i, ans[0], ans[1], ans[2], ans[3], ans[4], ans[5], ans[6], context_dict['hit']))
