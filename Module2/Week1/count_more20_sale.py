import pandas as pd
import numpy as np

data = pd.read_csv('Module2/Week1/advertising.csv').to_numpy()
counts = np.where(data[:,3]>=20,1,0).sum()
print(counts)