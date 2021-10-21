import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

ibovespa='^BVSP'
data_start = ["01-01-1994", "01-01-1998", "01-01-2002", "01-01-2006", "01-01-2010", "01-01-2014", "01-01-2018"]
data_end =   ["01-01-1995", "01-01-1999", "01-01-2003", "01-01-2007", "01-01-2011", "01-01-2015", "01-01-2019"]
position = 0

prices=pd.DataFrame()

for c in range(len(data_start)):
    resultado = wb.DataReader(ibovespa, data_source='yahoo', start=data_start[position], end=data_end[position])
    resultado["Adj Close"].plot()
    plt.show()
    position += 1
    #(resultado/resultado.iloc[0]*100).plot(figsize=(15,5))
    plt.ylabel('Preço Estável')
    plt.xlabel('Data')