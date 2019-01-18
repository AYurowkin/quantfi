import pandas as pd
from pathlib import Path


path = Path(__file__).parent / '../quantfi-backend/data-storage/daily_csv/MSFT_Daily.csv'
names = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
stock_df = pd.read_csv(path, names=names)

print(stock_df.shape)
stock_df.sample(5)