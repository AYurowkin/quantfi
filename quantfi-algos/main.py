from util.movingAverage import MovingAverage
from util.prep import Prep
from util.lstm import LSTM

# main class to run all tests


class Main:

    if __name__ == '__main__':
        p = Prep()
        stock_df = p.get_path('AAPL')
        lstm = LSTM()
        lstm.run_lstm(stock_df)
