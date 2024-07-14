import pandas as pd
import numpy as np

data = pd.read_csv('Module2/Week1/advertising.csv').to_numpy()
idx = data[:,3]-data[:,3].mean()
nearest_mean = idx[np.nonzero(abs(idx)==abs(idx).min())] + data[:,3].mean()
scores = np.where(data[:,3]>nearest_mean,'Good','Bad')
scores = np.where(data[:,3]==nearest_mean,'Average',scores)
print(scores[7:10])