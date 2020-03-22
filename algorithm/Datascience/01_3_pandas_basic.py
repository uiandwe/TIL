# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)


dates = pd.date_range('20130101', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)
print(df.index)
print(df.columns)
print(df.values)
print(df.info())

print(df['A'])
print(df[0:3])
print(df['20130102':'20130104'])
print(df.loc[dates[0]])
print(df.loc[:, ['A', 'B']])
print(df.loc['20130102':'20130104', ['A', 'B']])

print(df.iloc[3])

print(df[df > 0]) # 0 보다 큰 값만, 작으면 NaN

print("==================")
df2 = df.copy()

df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']

print(df2['E'].isin(['two', 'four']))

print(df2[df2['E'].isin(['two', 'four'])])

print("==================")

print(df.apply(np.cumsum)) # 누적 합

