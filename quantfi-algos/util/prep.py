from pathlib import Path
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Class that preps the stock data as a numpy array for LSTM


class Prep:
    def get_path(self, stock_name):
        stock_path = '../../quantfi-backend/data-storage/daily_csv_trim/' + stock_name + '_Daily_Trim.csv'
        path = Path(__file__).parent / stock_path
        stock_df = pd.read_csv(path)

        output = stock_df['Close'].values
        print(output)
        print(type(output))