import datetime as dt
import json
import os
import pandas as pd
from pandas.io.json import json_normalize

# Returns  pandas dataframe by fileName
def build_dataframe(fileName):

    # navigates to correct directory
    if 'data-storage' not in os.getcwd():
        os.chdir('quantfi-backend\data-storage')
   
    # opens file as read
    with open(fileName, 'r') as json_in:
        jsi = json.load(json_in)

    #converts time series data to pandas dataframe
    df = pd.DataFrame(jsi['Time Series (1min)'])
    df = df.T
    return df