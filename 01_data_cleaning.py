# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 16:33:56 2020

@author: Anastasia
"""
import pandas as pd
import numpy as np 

df_one = pd.read_csv('original_csvs/EtsySoldOrderItems2020.csv')
df_two = pd.read_csv('original_csvs/EtsySoldOrders2020.csv')

df = pd.merge(df_one, df_two, how='outer', on='Order ID', left_index=True, right_index=False)

print(df.columns)

df_clean= df.drop(['Sale Date_y','Date Posted_y','Delivery City_y','Delivery State_y','Delivery Zipcode_y','Delivery Country_y','Currency_y','Coupon Code_y','Coupon Details_y','Discount Amount_y','Delivery Discount_y','Buyer_y','Order Type_y', 'Payment Type_y', 'Currency_x','Delivery Address1','Delivery Address2','Delivery Zipcode_x','Order Type_x','Listings Type','Payment Type_x','InPerson Discount','InPerson Location', 'VAT Paid by Buyer','SKU', 'Full Name','Last Name','Payment Method','Status','Adjusted Order Total','Adjusted Card Processing Fees','Adjusted Net Order Amount', 'Street 1', 'Street 2'], axis=1)

print(df_clean.columns)


df_clean.rename(columns={'Sale Date_x':'Sale Date', 'Buyer_x':'Buyer','Coupon Code_x': 'Coupon Code', 'Coupon Details_x': 'Coupon Details', 'Discount Amount_x': 'Discount Amount', 'Delivery Discount_x': 'Delivery Discount', 'Date Posted_x': 'Date Posted', 'Delivery City_x': 'Delivery City', 'Delivery State_x': 'Delivery State', 'Delivery Country_x': 'Delivery Country'}, inplace=True)

print(df_clean.columns)