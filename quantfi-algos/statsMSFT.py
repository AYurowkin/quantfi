import pandas as pd
from pathlib import Path
import math
import matplotlib.pyplot as plt

path = Path(__file__).parent / '../quantfi-backend/data-storage/daily_csv_trim/MSFT_Daily.csv'
stock_df = pd.read_csv(path)
n = stock_df.shape[0]  # number of rows in stock list

# calculate mean and standard deviation of the closed price
mean = 0.0
for index, row in stock_df.iterrows():
    curr_close = row['Close']
    mean = mean + curr_close

mean = mean / n

std_dev = 0.0
for index, row in stock_df.iterrows():
    curr_close = row['Close']
    std_dev = std_dev + math.pow((curr_close - mean), 2)

std_dev = std_dev / n
std_dev = math.sqrt(std_dev)
print(mean)
print(std_dev)

# loop through the days of the year 2017 and calculate moving averages
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
