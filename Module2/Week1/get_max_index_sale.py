import pandas as pd 
import numpy as np

data = pd.read_csv('Module2/Week1/advertising.csv').to_numpy()
max_value = data[:,3].max()
idx = np.nonzero(data[:,3]==max_value)[0][0]
print(f"Max: {max_value} - Index: {idx}")