#%%
import datetime as dt
import json
import matplotlib.pyplot as plt
import os
import pandas as pd
from pandas.io.json import json_normalize


#%%
# navigates to correct directory
if 'data-storage' not in os.getcwd():
    os.chdir('quantfi-backend\data-storage')

#%%
with open('data.txt', 'r') as json_in:
    jsi = json.load(json_in)

df = pd.DataFrame(jsi['Time Series (1min)'])
df = df.T
df

#%%
df=df.astype(float)
#df.plot(use_index = True)
ax = df[['1. open', '2. high', '3. low', '4. close']].plot()
ax.set(ylabel = '$', xlabel = 'Time')
ax.plot(use_index = True)
plt.show()
