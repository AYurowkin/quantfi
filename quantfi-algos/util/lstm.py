from pathlib import Path
import numpy as np
import os
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import LSTM, Flatten
from keras.callbacks import CSVLogger
from keras import optimizers
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split


class LSTMModel:

    def build_data(self, df, index, step):
        dim_0 = df.shape[0] - step
        dim_1 = df.shape[1]
        x = np.zeros((dim_0, step, dim_1))
        y = np.zeros((dim_0, ))

        for i in range(dim_0):
            x[i] = df[i:step + i]
            y[i] = df[step + i, index]

        return x, y

    def drop_rows(self, df, batch_size):
        rows = df.shape[0] % batch_size
        if rows > 0:
            return df[:-rows]
        else:
            return df

    def run_lstm(self, stock_name):
        stock_path = '../../quantfi-backend/data-storage/daily_csv_trim/' + stock_name + '_Daily_Trim.csv'
        path = Path(__file__).parent / stock_path
        stock_df = pd.read_csv(path)

        # global variables that will be needed
        columns = ["Open", "High", "Low", "Close", "Volume"]
        time_step = 30
        output_col_index = 3
        batch_size = 20
        learning_rate = 0.0001
        epochs = 300
        log_path = os.path.join('../../quantfi-backend/data-storage/logs/lstm_log.log')
        log_path = Path(__file__).parent / log_path

        # split into train and test set
        stock_train, stock_test = train_test_split(stock_df, train_size=0.8, test_size=0.2, shuffle=False)
        print("Train and Test size", len(stock_train), len(stock_test))

        # scaling
        x = stock_train.loc[:, columns].values
        mms = MinMaxScaler()
        x_train = mms.fit_transform(x)
        x_test = mms.transform(stock_test.loc[:, columns])

        # organize data to feed to model
        train_x, train_y = self.build_data(x_train, output_col_index, time_step)
        train_x = self.drop_rows(train_x, batch_size)
        train_y = self.drop_rows(train_y, batch_size)

        val_test_x, val_test_y = self.build_data(x_test, output_col_index, time_step)
        val_x, test_x = np.split(self.drop_rows(val_test_x, batch_size), 2)
        val_y, test_y = np.split(self.drop_rows(val_test_y, batch_size), 2)

        # build model
        model = Sequential()
        model.add(LSTM(100, batch_input_shape=(batch_size, time_step, train_x.shape[2]), dropout=0.0, recurrent_dropout=0.0, stateful=True, return_sequences=True, kernel_initializer='random_uniform'))
        model.add(Dropout(0.4))
        model.add(LSTM(60, dropout=0.0))
        model.add(Dropout(0.4))
        model.add(Dense(20, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))
        optimizer = optimizers.RMSprop(lr=learning_rate)
        model.compile(loss='mean_squared_error', optimizer=optimizer, metrics=['accuracy'])
        csv_logger = CSVLogger(log_path, append=True)
        model.fit(train_x, train_y, epochs=epochs, verbose=2, batch_size=batch_size, shuffle=False, validation_data=(self.drop_rows(val_x, batch_size), self.drop_rows(val_y, batch_size)), callbacks=[csv_logger])

    def lstm_practice(self):
        stock_path = '../../quantfi-backend/data-storage/daily_csv_trim/AAPL_Daily_Trim.csv'
        path = Path(__file__).parent / stock_path
        stock_df = pd.read_csv(path)
        stock_df = stock_df.sort_values('Date')
        high_prices = stock_df.loc[:, 'High'].as_matrix()
        low_prices = stock_df.loc[:, 'Low'].as_matrix()
        volume = stock_df.loc[:, 'Volume'].as_matrix()
        mid_prices = (high_prices + low_prices) / 2.00

        split = round(0.8 * stock_df.shape[0])

        train_data = mid_prices[:split]
        test_data = mid_prices[split:]

        train_vol_data = volume[:split]
        test_vol_data = volume[split:]

        print(train_vol_data.shape)
        print(test_vol_data.shape)
        print(train_data.shape)
        print(test_data.shape)

        # mnist = tf.keras.datasets.mnist
        # (x_train, y_train), (x_test, y_test) = mnist.load_data()
        #
        # x_train = x_train / 255.0
        # x_test = x_test / 255.0
        #
        # model = Sequential()
        #
        # model.add(LSTM(128, input_shape=(x_train.shape[1:]), activation='relu', return_sequences=True))
        # model.add(Dropout(0.2))
        #
        # model.add(LSTM(128, activation='relu'))
        # model.add(Dropout(0.2))
        #
        # model.add(Dense(32, activation='relu'))
        # model.add(Dropout(0.2))
        #
        # model.add(Dense(10, activation='softmax'))
        #
        # opt = tf.keras.optimizers.Adam(lr=1e-3, decay=1e-5)
        #
        # model.compile(loss='sparse_categorical_crossentropy',
        #               optimizer=opt,
        #               metrics=['accuracy'])
        #
        # model.fit(x_train, y_train, epochs=3, validation_data=(x_test, y_test))


