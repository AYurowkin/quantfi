import tensorflow as tf
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Dropout, LSTM, CuDNNLSTM
from pathlib import Path
import pandas as pd


stock_path = '../../quantfi-backend/data-storage/daily_csv_trim/AAPL_Daily_Trim.csv'
path = Path(__file__).parent / stock_path
stock_df = pd.read_csv(path)

stock_df = stock_df.sort_values('Date')
high_prices = stock_df.loc[:, 'High'].as_matrix()
low_prices = stock_df.loc[:, 'Low'].as_matrix()
mid_prices = (high_prices + low_prices) / 2.00

train_val = 0.8 * stock_df.shape[0]
test_val = 0.2 * stock_df.shape[1]




mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train/255.0
x_test = x_test/255.0

model = Sequential()

model.add(LSTM(128, input_shape=(x_train.shape[1:]), activation='relu', return_sequences=True))
# model.add(CuDNNLSTM(128, input_shape=(x_train.shape[1:]), return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(128, activation='relu'))
# model.add(CuDNNLSTM(128))
model.add(Dropout(0.2))

model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(10, activation='softmax'))

opt = tf.keras.optimizers.Adam(lr=1e-3, decay=1e-5)

model.compile(loss='sparse_categorical_crossentropy',
              optimizer=opt,
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=3, validation_data=(x_test, y_test))
