from util.movingAverage import MovingAverage
from util.prep import Prep

# main class to run all tests


class Main:

    if __name__ == '__main__':
        p = Prep()
        p.get_path('AAPL')
        ma = MovingAverage(20, 100)
        ma.get_one_ma_intersection('AAPL')
