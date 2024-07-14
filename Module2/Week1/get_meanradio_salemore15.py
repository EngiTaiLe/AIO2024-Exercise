import pandas as pd 
import numpy as np

data = pd.read_csv('Module2/Week1/advertising.csv').to_numpy()
mean_value = data[np.nonzero(data[:,3]>=15),1].mean()
print(mean_value)