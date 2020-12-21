# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 16:33:56 2020

@author: Anastasia
"""
import pandas as pd
import numpy as np 

df_one = pd.read_csv('original_csvs/EtsySoldOrderItems2020.csv')
df_two = pd.read_csv('original_csvs/EtsySoldOrders2020.csv')

print(df_one.head())
print(df_two.head())

df = pd.merge(df_one, df_two, how='outer', on='Order ID', left_index=True, right_index=False)

print(df.head())