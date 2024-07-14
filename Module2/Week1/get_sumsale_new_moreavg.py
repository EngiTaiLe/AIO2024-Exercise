import pandas as pd
import numpy as np

data = pd.read_csv('Module2/Week1/advertising.csv').to_numpy()
sum_value = data[np.nonzero(data[:,2]>data[:,2].mean()),3].sum()
print(sum_value)