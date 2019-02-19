from pathlib import Path
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# class that plots two N moving averages and finds the intersections


class MovingAverage:
    # variables to hold the given two days for plotting moving averages
    day_one = 0
    day_two = 0

    def __init__(self, d1, d2):
        self.day_one = d1
        self.day_two = d2

    # plot the moving average of a given stock

    def get_ma_one_stock(self, stock_name):
        stock_path = '../../quantfi-backend/data-storage/daily_csv_trim/' + stock_name + '_Daily_Trim.csv'
        path = Path(__file__).parent / stock_path
        stock_df = pd.read_csv(path)

        n = stock_df.shape[0]  # number of rows in stock list
        if n < 252:
            print('Stock data insufficient')
        else:
            # loop through the days of the year 2017 and calculate moving averages
            first_day = stock_df.Date.str.startswith('2016').idxmax() - 1
            day_one = self.day_one
            day_two = self.day_two
            day_one_avg = []
            day_two_avg = []
            for i in range(first_day, 0, -1):
                day_one_avg.append((sum(stock_df['Close'].iloc[i:i + day_one].values)) / day_one)
                day_two_avg.append((sum(stock_df['Close'].iloc[i:i + day_two].values)) / day_two)

            # truncate to four decimals in both MA arrays
            day_one_avg_trunc = np.array(day_one_avg)
            day_two_avg_trunc = np.array(day_two_avg)
            num_decimals = 10
            decade = 10 ** num_decimals
            day_one_avg_trunc = np.trunc(day_one_avg_trunc * decade) / decade
            day_two_avg_trunc = np.trunc(day_two_avg_trunc * decade) / decade

            # create two 2d arrays from days and ma arrays for 30 days and 90 days
            days = np.array(list(range(0, first_day, 1)))  # 251 stock days in a calendar year (0 - 250)
            inter_day_one = np.column_stack((days, day_one_avg_trunc))
            inter_day_two = np.column_stack((days, day_two_avg_trunc))

            # find intersection with system of equations
            intersection = []
            for row in (days - 1):
                # get x, y pairs of the current day
                curr_x_day_one = inter_day_one[row][0]
                curr_y_day_one = inter_day_one[row][1]
                curr_x_day_two = inter_day_two[row][0]
                curr_y_day_two = inter_day_two[row][1]
                # get x, y pairs of the next day
                next_x_day_one = inter_day_one[row + 1][0]
                next_y_day_one = inter_day_one[row + 1][1]
                next_x_day_two = inter_day_two[row + 1][0]
                next_y_day_two = inter_day_two[row + 1][1]

                # create point tuples
                curr_points_day_one = [curr_x_day_one, curr_y_day_one]
                next_points_day_one = [next_x_day_one, next_y_day_one]
                curr_points_day_two = [curr_x_day_two, curr_y_day_two]
                next_points_day_two = [next_x_day_two, next_y_day_two]

                # create the lines
                a_day_one = curr_points_day_one[1] - next_points_day_one[1]
                b_day_one = next_points_day_one[0] - curr_points_day_one[0]
                c_day_one = curr_points_day_one[0] * next_points_day_one[1] - next_points_day_one[0] * curr_points_day_one[1]
                a_day_two = curr_points_day_two[1] - next_points_day_two[1]
                b_day_two = next_points_day_two[0] - curr_points_day_two[0]
                c_day_two = curr_points_day_two[0] * next_points_day_two[1] - next_points_day_two[0] * curr_points_day_two[1]

                line_day_one = a_day_one, b_day_one, -c_day_one
                line_day_two = a_day_two, b_day_two, -c_day_two

                # find intersections
                d = line_day_one[0] * line_day_two[1] - line_day_one[1] * line_day_two[0]
                dx = line_day_one[2] * line_day_two[1] - line_day_one[1] * line_day_two[2]
                dy = line_day_one[0] * line_day_two[2] - line_day_one[2] * line_day_two[0]
                if d != 0:
                    x = dx / d
                    y = dy / d
                    # make sure intersection is within the bounds
                    if curr_x_day_one <= x <= next_x_day_one:
                        intersection.append([x, y])

            # plot MA
            plt.plot(days, day_one_avg_trunc, label=str(day_one) + ' MA')
            plt.plot(days, day_two_avg_trunc, label=str(day_two) + ' MA')
            plt.legend(loc='upper right')
            # get name of stock
            plt.title(s=stock_name, color='green')
            plt.xlabel(s='Day', color='green')
            plt.ylabel(s='Price', color='green')

            # plot intersection
            x_val = [x[0] for x in intersection]
            y_val = [y[1] for y in intersection]
            plt.scatter(x_val, y_val, color='red')
            plt.show()

    def get_all_ma(self):
        # modularize csv trim such that you can plot all moving averages for all the stocks
        path = '../quantfi-backend/data-storage/daily_csv_trim/'
        directory = os.fsencode(path)

        # loop through directory to get each stock CSV
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.endswith(".csv"):
                curr_file_path = '../../quantfi-backend/data-storage/daily_csv_trim/' + filename
                stock_path = Path(__file__).parent / curr_file_path
                # store csv data
                stock_df = pd.read_csv(stock_path)
                n = stock_df.shape[0]  # number of rows in stock list

                # check if current stock has sufficient data
                if n < 252:
                    continue
                else:
                    # loop through the days of the year 2017 and calculate moving averages
                    first_day = stock_df.Date.str.startswith('2016').idxmax() - 1
                    day_one = self.day_one
                    day_two = self.day_two
                    day_one_avg = []
                    day_two_avg = []
                    for i in range(first_day, 0, -1):
                        day_one_avg.append((sum(stock_df['Close'].iloc[i:i + day_one].values)) / day_one)
                        day_two_avg.append((sum(stock_df['Close'].iloc[i:i + day_two].values)) / day_two)

                    # truncate to four decimals in both MA arrays
                    day_one_avg_trunc = np.array(day_one_avg)
                    day_two_avg_trunc = np.array(day_two_avg)
                    num_decimals = 10
                    decade = 10 ** num_decimals
                    day_one_avg_trunc = np.trunc(day_one_avg_trunc * decade) / decade
                    day_two_avg_trunc = np.trunc(day_two_avg_trunc * decade) / decade

                    # create two 2d arrays from days and ma arrays for 30 days and 90 days
                    days = np.array(list(range(0, first_day, 1)))  # 251 stock days in a calendar year (0 - 250)
                    inter_day_one = np.column_stack((days, day_one_avg_trunc))
                    inter_day_two = np.column_stack((days, day_two_avg_trunc))

                    # find intersection with system of equations
                    intersection = []
                    for row in (days - 1):
                        # get x, y pairs of the current day
                        curr_x_day_one = inter_day_one[row][0]
                        curr_y_day_one = inter_day_one[row][1]
                        curr_x_day_two = inter_day_two[row][0]
                        curr_y_day_two = inter_day_two[row][1]
                        # get x, y pairs of the next day
                        next_x_day_one = inter_day_one[row + 1][0]
                        next_y_day_one = inter_day_one[row + 1][1]
                        next_x_day_two = inter_day_two[row + 1][0]
                        next_y_day_two = inter_day_two[row + 1][1]

                        # create point tuples
                        curr_points_day_one = [curr_x_day_one, curr_y_day_one]
                        next_points_day_one = [next_x_day_one, next_y_day_one]
                        curr_points_day_two = [curr_x_day_two, curr_y_day_two]
                        next_points_day_two = [next_x_day_two, next_y_day_two]

                        # create the lines
                        a_day_one = curr_points_day_one[1] - next_points_day_one[1]
                        b_day_one = next_points_day_one[0] - curr_points_day_one[0]
                        c_day_one = curr_points_day_one[0] * next_points_day_one[1] - next_points_day_one[0] * \
                                    curr_points_day_one[1]
                        a_day_two = curr_points_day_two[1] - next_points_day_two[1]
                        b_day_two = next_points_day_two[0] - curr_points_day_two[0]
                        c_day_two = curr_points_day_two[0] * next_points_day_two[1] - next_points_day_two[0] * \
                                    curr_points_day_two[1]

                        line_day_one = a_day_one, b_day_one, -c_day_one
                        line_day_two = a_day_two, b_day_two, -c_day_two

                        # find intersections
                        d = line_day_one[0] * line_day_two[1] - line_day_one[1] * line_day_two[0]
                        dx = line_day_one[2] * line_day_two[1] - line_day_one[1] * line_day_two[2]
                        dy = line_day_one[0] * line_day_two[2] - line_day_one[2] * line_day_two[0]
                        if d != 0:
                            x = dx / d
                            y = dy / d
                            # make sure intersection is within the bounds
                            if curr_x_day_one <= x <= next_x_day_one:
                                intersection.append([x, y])

                    # plot MA
                    plt.plot(days, day_one_avg_trunc, label=str(day_one) + ' MA')
                    plt.plot(days, day_two_avg_trunc, label=str(day_two) + ' MA')
                    plt.legend(loc='upper right')
                    # get name of stock
                    plt.title(s=filename.split("_", 1)[0], color='green')
                    plt.xlabel(s='Day', color='green')
                    plt.ylabel(s='Price', color='green')

                    # plot intersection
                    x_val = [x[0] for x in intersection]
                    y_val = [y[1] for y in intersection]
                    plt.scatter(x_val, y_val, color='red')
                    plt.show()