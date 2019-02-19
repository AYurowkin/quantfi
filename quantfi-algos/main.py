from util.movingAverage import MovingAverage

# main class to run all tests


class Main:

    if __name__ == '__main__':
        ma = MovingAverage(30, 90)
        ma.get_ma_one_stock('AABA')
