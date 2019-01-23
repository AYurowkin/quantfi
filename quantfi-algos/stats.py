import os
import pandas as pd
from pathlib import Path
import math
import matplotlib.pyplot as plt

# modularize csv trim such that you can plot all moving averages for all the stocks
path = '../quantfi-backend/data-storage/daily_csv_trim/'
directory = os.fsencode(path)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".csv"):
        print(filename)
    else:
        continue
