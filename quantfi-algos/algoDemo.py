import pandas as pd
from pathlib import Path


path = Path(__file__).parent / '../quantfi-backend/data-storage/daily_csv/MSFT_Daily.csv'
stock_df = pd.read_csv(path)
print(stock_df)