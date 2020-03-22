# -*- coding: utf-8 -*-
import pandas as pd
import os

now_path = os.path.dirname(os.path.realpath(__file__))

CCTV_Seoul = pd.read_csv(os.path.join(now_path, "data/01. CCTV_in_Seoul.csv"), encoding='utf-8')
print(CCTV_Seoul.head())

print(CCTV_Seoul.columns) # Index(['기관명', '소계', '2013년도 이전', '2014년', '2015년', '2016년'], dtype='object')

print(CCTV_Seoul.columns[0]) # 기과명

CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0]: '구별'}, inplace=True) # 기관명 -> 구별

print(CCTV_Seoul.head())
