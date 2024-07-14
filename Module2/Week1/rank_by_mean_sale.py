import pandas as pd
import numpy as np

data = pd.read_csv('Module2/Week1/advertising.csv').to_numpy()
scores = np.where(data[:,3]>data[:,3].mean(),'Good','Bad')
scores = np.where(data[:,3]==data[:,3].mean(),'Average',scores)
print(scores[7:10])