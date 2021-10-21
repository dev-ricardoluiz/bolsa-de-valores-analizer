# importações
from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt

# define ticker e espaço de tempo
data_start = "01-01-1970"
data_end =  "10-20-2021"
cotacao_ibov = web.DataReader('^BVSP', data_source='yahoo', start=data_start, end=data_end)
# mostra tabela
#print(cotacao_ibov)

# mostra gráfico
cotacao_ibov["Adj Close"].plot()
plt.show()