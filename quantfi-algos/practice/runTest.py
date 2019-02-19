from practice.graphDataFrame import graph_dataframe
from pathlib import Path


#%%
# generate path for specific file, need to modularize this later
path = Path(__file__).parent / '../../quantfi-backend/data-storage/daily_txt/MSFT_Daily.txt'
plt = graph_dataframe(path)
plt.show()
