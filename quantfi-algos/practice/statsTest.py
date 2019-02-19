from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# test file to test operations on a single stock
# change stock name in path to use a different stock
path = Path(__file__).parent / '../../quantfi-backend/data-storage/daily_csv_trim/AMCN_Daily_Trim.csv'
stock_df = pd.read_csv(path)
n = stock_df.shape[0]  # number of rows in stock list

# loop through the days of the year 2017 and calculate moving averages
first_day = stock_df.Date.str.startswith('2016').idxmax() - 1

thirty = 30
ninety = 90
thirty_day_avg = []
ninety_day_avg = []
for i in range(first_day, 0, -1):
    thirty_day_avg.append((sum(stock_df['Close'].iloc[i:i + thirty].values)) / thirty)
    ninety_day_avg.append((sum(stock_df['Close'].iloc[i:i + ninety].values)) / ninety)

# truncate to four decimals in both MA arrays
thirty_day_avg_trunc = np.array(thirty_day_avg)
ninety_day_avg_trunc = np.array(ninety_day_avg)
num_decimals = 10
decade = 10**num_decimals
thirty_day_avg_trunc = np.trunc(thirty_day_avg_trunc*decade) / decade
ninety_day_avg_trunc = np.trunc(ninety_day_avg_trunc*decade) / decade

# create two 2d arrays from days and ma arrays for 30 days and 90 days
days = np.array(list(range(0, first_day, 1)))  # 251 stock days in a calendar year (0 - 250)
inter_30 = np.column_stack((days, thirty_day_avg_trunc))
inter_90 = np.column_stack((days, ninety_day_avg_trunc))

# find intersection with system of equations
intersection = []
for row in (days - 1):
    # get x, y pairs of the current day
    curr_x_30 = inter_30[row][0]
    curr_y_30 = inter_30[row][1]
    curr_x_90 = inter_90[row][0]
    curr_y_90 = inter_90[row][1]
    # get x, y pairs of the next day
    next_x_30 = inter_30[row+1][0]
    next_y_30 = inter_30[row+1][1]
    next_x_90 = inter_90[row+1][0]
    next_y_90 = inter_90[row+1][1]

    # create point tuples
    curr_points_30 = [curr_x_30, curr_y_30]
    next_points_30 = [next_x_30, next_y_30]
    curr_points_90 = [curr_x_90, curr_y_90]
    next_points_90 = [next_x_90, next_y_90]

    # create the lines
    a_30 = curr_points_30[1] - next_points_30[1]
    b_30 = next_points_30[0] - curr_points_30[0]
    c_30 = curr_points_30[0] * next_points_30[1] - next_points_30[0] * curr_points_30[1]
    a_90 = curr_points_90[1] - next_points_90[1]
    b_90 = next_points_90[0] - curr_points_90[0]
    c_90 = curr_points_90[0] * next_points_90[1] - next_points_90[0] * curr_points_90[1]

    l1 = a_30, b_30, -c_30
    l2 = a_90, b_90, -c_90

    # find intersections
    d = l1[0] * l2[1] - l1[1] * l2[0]
    dx = l1[2] * l2[1] - l1[1] * l2[2]
    dy = l1[0] * l2[2] - l1[2] * l2[0]
    if d != 0:
        x = dx / d
        y = dy / d
        # make sure intersection is within the bounds
        if curr_x_30 <= x <= next_x_30:
            intersection.append([x, y])

# plot MA
plt.plot(days, thirty_day_avg_trunc, label='30 MA')
plt.plot(days, ninety_day_avg_trunc, label='90 MA')
plt.legend(loc='upper right')

# plot intersection
x_val = [x[0] for x in intersection]
y_val = [y[1] for y in intersection]
plt.scatter(x_val, y_val, color='red')

plt.show()
