# -*- coding: utf-8 -*-
import pandas_datareader.data as web
import yfinance as yf
import matplotlib.pyplot as plt


yf.pdr_override()

data = web.get_data_yahoo('AAPL', start="2010-01-01", end="2020-01-01")

plt.plot(data.index, data['Adj Close'])
plt.show()
