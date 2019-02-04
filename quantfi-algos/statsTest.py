import pandas as pd
from pathlib import Path
import math
import matplotlib.pyplot as plt
import numpy as np

path = Path(__file__).parent / '../quantfi-backend/data-storage/daily_csv_trim/ALOT_Daily_Trim.csv'
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

# truncate all decimals in both MA arrays
thirty_day_avg_trunc = np.array(thirty_day_avg)
ninety_day_avg_trunc = np.array(ninety_day_avg)
num_decimals = 4
decade = 10**num_decimals
thirty_day_avg_trunc = np.trunc(thirty_day_avg_trunc*decade) / decade
ninety_day_avg_trunc = np.trunc(ninety_day_avg_trunc*decade) / decade

# calculate intersection between 30 and 90 day MA
diff = []
while i < first_day - 1:
    # create a linear equation for both 30 and 90 day MA
    x1_thirty = i
    x2_thirty = i + 4
    y1_thirty = thirty_day_avg_trunc[i]
    y2_thirty = thirty_day_avg_trunc[i+1]
    m_thirty = (y1_thirty - y2_thirty) / (x1_thirty - x2_thirty)
    b_thirty = ((x1_thirty * y1_thirty) - (x2_thirty * y1_thirty)) / (x1_thirty - x2_thirty)
    x1_ninety = i
    x2_ninety = i + 1
    y1_ninety = ninety_day_avg_trunc[i]
    y2_ninety = ninety_day_avg_trunc[i+1]
    m_ninety = (y1_ninety - y2_ninety) / (x1_ninety - x2_ninety)
    b_ninety = ((x1_ninety * y1_ninety) - (x2_ninety * y2_ninety) / (x1_ninety - x2_ninety))
    # y = m_thirty*x + b_thirty
    # put in form x + y = b
    m_thirty = 0 - m_thirty
    m_ninety = 0 - m_ninety
    a = np.array([[m_thirty, m_ninety], [1, 1]])
    b = np.array([b_thirty, b_ninety])
    intersection = np.linalg.solve(a, b)
    # need to figure out how to plot the intersections
    np.append(diff, intersection)
    print(intersection)
    i += 5

# create a 2d array from days and ma arrays for 30 days and 90 days


# plot MA
days = list(range(0, first_day, 1))  # 251 stock days in a calendar year (0 - 250)
plt.plot(days, thirty_day_avg_trunc, label='30 MA')
plt.plot(days, ninety_day_avg_trunc, label='90 MA')
plt.legend(loc='upper right')

# plot intersection
x_val = [x[0] for x in diff]
y_val = [x[1] for x in diff]
plt.plot(x_val, y_val, color='red')

plt.show()
