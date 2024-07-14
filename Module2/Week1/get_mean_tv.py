import pandas as pd 
import numpy as np

data = pd.read_csv('Module2/Week1/advertising.csv').to_numpy()
mean_tv = np.mean(data[:,0])
print(mean_tv)
