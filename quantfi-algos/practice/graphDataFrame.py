from practice.buildDataFrame import build_dataframe
import matplotlib.pyplot as plt


# Returns plt plot of dataframe by fileName
def graph_dataframe(file_name):
    df = build_dataframe(file_name)
    df = df.astype(float)
    ax = df[['1. open', '2. high', '3. low', '4. close']].plot()
    ax.set(ylabel='$', xlabel='Time')
    ax.plot(use_index=True)
    return plt
