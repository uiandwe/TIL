# -*- coding: utf-8 -*-
import pandas_datareader.data as web
import datetime

start = datetime.datetime(2016, 2, 19)
end = datetime.datetime(2016, 3, 4)

gs = web.DataReader('078930.KS', 'yahoo', start, end)

print(gs.info())
print(gs.head())


import matplotlib.pyplot as plt

plt.plot(gs['Close'])
plt.show()
