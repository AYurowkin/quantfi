import pandas as pd
from pathlib import Path

# should delete this file at some point because this is handle in dailyConversionTrim in Conversion.java
path = Path(__file__).parent / '../quantfi-backend/data-storage/daily_csv/MSFT_Daily.csv'
stock_df = pd.read_csv(path)

for index, row in stock_df.iterrows():
    curr_date = row['Date']
    curr_date = curr_date[:4]
    if any([int(curr_date) > 2018, int(curr_date) < 2012]):
        stock_df.drop(index, inplace=True)

save_path = Path(__file__).parent / '../quantfi-backend/data-storage/daily_csv_trim/MSFT_Daily.csv'
stock_df.to_csv(save_path, encoding='utf-8', index=False)
