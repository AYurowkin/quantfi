from util.movingAverage import MovingAverage

# main class to run all tests


class Main:

    if __name__ == '__main__':
        ma = MovingAverage(20, 100)
        ma.get_one_ma_intersection('AAPL')
