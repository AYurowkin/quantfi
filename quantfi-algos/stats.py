import os
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# modularize csv trim such that you can plot all moving averages for all the stocks
path = '../quantfi-backend/data-storage/daily_csv_trim/'
directory = os.fsencode(path)

# loop through directory to get each stock CSV
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".csv"):
        curr_file_path = '../quantfi-backend/data-storage/daily_csv_trim/' + filename
        stock_path = Path(__file__).parent / curr_file_path
        stock_df = pd.read_csv(stock_path)

        first_day = stock_df.Date.str.startswith('2016').idxmax() - 1
        # check to see if data has year 2016
        if first_day != -1:
            thirty = 30
            ninety = 90
            thirty_day_avg = []
            ninety_day_avg = []
            # calculate MA for current stock
            for i in range(first_day, 0, -1):
                thirty_day_avg.append((sum(stock_df['Close'].iloc[i:i + thirty].values)) / thirty)
                ninety_day_avg.append((sum(stock_df['Close'].iloc[i:i + ninety].values)) / ninety)

            days = list(range(0, first_day, 1))  # 251 stock days in a calendar year (0 - 250)
            plt.plot(days, thirty_day_avg)
            plt.plot(days, ninety_day_avg)
            first_day = stock_df.Date.str.startswith('2016').idxmax() - 1
            thirty = 30
            ninety = 90
            thirty_day_avg = []
            ninety_day_avg = []
            for i in range(first_day, 0, -1):
                thirty_day_avg.append((sum(stock_df['Close'].iloc[i:i + thirty].values)) / thirty)
                ninety_day_avg.append((sum(stock_df['Close'].iloc[i:i + ninety].values)) / ninety)

            days = list(range(0, first_day, 1))  # 251 stock days in a calendar year (0 - 250)
            plt.plot(days, thirty_day_avg)
            plt.plot(days, ninety_day_avg)
            plt.show()
        else:
            continue
    else:
        continue
