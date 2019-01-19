import pandas as pd
from pathlib import Path
import math


path = Path(__file__).parent / '../quantfi-backend/data-storage/daily_csv_trim/MSFT_Daily.csv'
stock_df = pd.read_csv(path)
n = stock_df.shape[0]   # number of rows in stock list

# calculate mean and standard deviation of the closed price
mean = 0.0
for index, row in stock_df.iterrows():
    curr_close = row["Close"]
    mean = mean + curr_close

mean = mean / n

std_dev = 0.0
for index, row in stock_df.iterrows():
    curr_close = row["Close"]
    std_dev = std_dev + math.pow((curr_close - mean), 2)

std_dev = std_dev / n
std_dev = math.sqrt(std_dev)
print(mean)
print(std_dev)
print(stock_df)
