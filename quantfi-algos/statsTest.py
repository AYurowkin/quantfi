import pandas as pd
from pathlib import Path
import math
import matplotlib.pyplot as plt
import numpy as np
import itertools

path = Path(__file__).parent / '../quantfi-backend/data-storage/daily_csv_trim/ASGN_Daily_Trim.csv'
stock_df = pd.read_csv(path)
n = stock_df.shape[0]  # number of rows in stock list

# calculate mean and standard deviation of the closed price
mean = 0.0
for index, row in stock_df.iterrows():
    curr_close = row['Close']
    mean = mean + curr_close

mean = mean / n
# print(mean)

std_dev = 0.0
for index, row in stock_df.iterrows():
    curr_close = row['Close']
    std_dev = std_dev + math.pow((curr_close - mean), 2)

std_dev = std_dev / n
std_dev = math.sqrt(std_dev)
# print(std_dev)

# loop through the days of the year 2017 and calculate moving averages
first_day = stock_df.Date.str.startswith('2016').idxmax() - 1
# print(stock_df.Date)

thirty = 30
ninety = 90
thirty_day_avg = []
ninety_day_avg = []
for i in range(first_day, 0, -1):
    thirty_day_avg.append((sum(stock_df['Close'].iloc[i:i + thirty].values)) / thirty)
    ninety_day_avg.append((sum(stock_df['Close'].iloc[i:i + ninety].values)) / ninety)
    # print(thirty_day_avg)
    # print(ninety_day_avg)

# truncate to four decimals in both MA arrays
thirty_day_avg_trunc = np.array(thirty_day_avg)
ninety_day_avg_trunc = np.array(ninety_day_avg)
num_decimals = 4
# TODO: need to figure out how many decimals for average price, right now it's truncating to 4 decimal places
decade = 10**num_decimals
thirty_day_avg_trunc = np.trunc(thirty_day_avg_trunc*decade) / decade
ninety_day_avg_trunc = np.trunc(ninety_day_avg_trunc*decade) / decade

# create two 2d arrays from days and ma arrays for 30 days and 90 days
days = np.array(list(range(0, first_day, 1)))  # 251 stock days in a calendar year (0 - 250)
inter_30 = np.column_stack((days, thirty_day_avg_trunc))
inter_90 = np.column_stack((days, ninety_day_avg_trunc))
intersection = np.empty((0, 2))

# loop through the 2d arrays and find the x y pairs of intersection
# TODO: need to figure out the appropriate tolerance, right now it's 3*(10)^-2
for i, j in itertools.product(np.arange(inter_30.shape[0]), np.arange(inter_90.shape[0])):
    if np.all(np.isclose(inter_30[i], inter_90[j], atol=3e-2)):
        intersection = np.concatenate((intersection, [inter_90[j]]), axis=0)
# TODO: figure out how to solve the overestimation of intersections
print(stock_df)
print("INTERSECTION DATA")
print(intersection)


# plot MA
plt.plot(days, thirty_day_avg_trunc, label='30 MA')
plt.plot(days, ninety_day_avg_trunc, label='90 MA')
plt.legend(loc='upper right')

# plot intersection
x_val = [x[0] for x in intersection]
y_val = [x[1] for x in intersection]
plt.scatter(x_val, y_val, color='red')

plt.show()
