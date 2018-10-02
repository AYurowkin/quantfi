#%%
import datetime as dt
import json
import matplotlib.pyplot as plt
import os
import pandas as pd
from pandas.io.json import json_normalize


#%%
# navigates to correct directory
if 'quantfi-algos' not in os.getcwd():
    os.chdir('quantfi-algos')

with open('data.txt', 'r') as json_in:
    jsi = json.load(json_in)
df = pd.DataFrame.from_dict(jsi, orient='columns')
df