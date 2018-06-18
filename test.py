import pickle
import pandas as pd

x1 = []
with open('songs', 'rb') as f:
    x1 = pickle.load(f)

a1 = pd.DataFrame(x1).transpose()

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

t = a1[2001].values
plt.hist(t, bins=np.arange(t.min(), t.max()+1))
plt.show()
