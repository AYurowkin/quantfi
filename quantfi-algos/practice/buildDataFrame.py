import json
import pandas as pd


# Returns  pandas dataframe by fileName
def build_dataframe(file_name):
    # opens file as read
    with open(file_name, 'r') as json_in:
        jsi = json.load(json_in)

    # converts time series data to pandas dataframe
    df = pd.DataFrame(jsi['Time Series (Daily)'])
    df = df.T
    return df