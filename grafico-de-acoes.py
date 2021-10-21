import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

TickerA='ITSA4.SA'
TickerB='FLRY3.SA'
TickerC='LREN3.SA'
TickerD='PRIO3.SA'
TickerE='BPAN4.SA'
TickerF='LWSA3.SA'

prices=pd.DataFrame()
tickers = [TickerA, TickerB, TickerC, TickerD, TickerE, TickerF]
for t in tickers:
    prices[t]=wb.DataReader(t, data_source='yahoo', start='2019-1-1')['Adj Close']

(prices/prices.iloc[0]*100).plot(figsize=(15,5))
plt.ylabel('NORMALIZED PRICES')
plt.xlabel('DATE')
plt.show()