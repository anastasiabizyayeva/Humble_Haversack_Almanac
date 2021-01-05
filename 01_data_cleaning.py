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

df_clean= df.drop(['Sale Date_y','Date Posted_y','Delivery City_y','Delivery State_y','Delivery Zipcode_y','Delivery Country_y','Currency_y','Coupon Code_y','Coupon Details_y','Discount Amount_y','Delivery Discount_y','Buyer_x','Order Type_y', 'Payment Type_y', 'Currency_x','Delivery Address1','Delivery Address2','Delivery Zipcode_x','Order Type_x','Listings Type','Payment Type_x','InPerson Discount','InPerson Location', 'VAT Paid by Buyer','SKU','Last Name','Payment Method','Status','Adjusted Order Total','Adjusted Card Processing Fees','Adjusted Net Order Amount', 'Street 1', 'Street 2'], axis=1)

df_clean.rename(columns={'Sale Date_x':'Sale Date', 'Buyer_y':'Buyer','Coupon Code_x': 'Coupon Code', 'Coupon Details_x': 'Coupon Details', 'Discount Amount_x': 'Discount Amount', 'Delivery Discount_x': 'Delivery Discount', 'Date Posted_x': 'Date Posted', 'Delivery City_x': 'Delivery City', 'Delivery State_x': 'Delivery State', 'Delivery Country_x': 'Delivery Country'}, inplace=True)

df_clean['Buyer'] = df_clean['Buyer'].str.lower()
df_clean['Buyer First Name'] = df_clean['Buyer'].str.split(' ').str[0]

clean_descriptions = {
    'DnD Stickers / D20 Stickers / Emoji Stickers / Cute RPG, Fantasy Stickers / Red D20 Stickers / Matte Stickers': 'Red Sticker',
    'DnD Stickers / D20 Stickers / Emoji Stickers / Cute RPG, Fantasy Stickers / Rainbow D20 Stickers / Matte Stickers': 'Rainbow Sticker',
    'DnD Postcard / D&D Postcard / DnD Card / D20 Postcard / D20 Card / Dreamy Dice / Dice Card / DnD Print / Dice Print / Fantasy Art Print': 'Dice Postcard',
    'Shiba Inu Postcard / Dog Postcard / Puppy Postcard / Shiba Inu Card / Shiba Postcard / Puppy Card / Shiba Print / Dog Print / A6': 'Shiba Inu Postcard',
    'DnD Birthday Card/ D&D Card / Dungeon Master Card / D20 / Natural 20 / Age Modifier / Tabletop RPG Gaming / DnD Greeting Card / A6': 'Age Modifier Card',
    'DnD Birthday Card/ D&D Card / Dungeon Master Card / D20 / Natural 20 / Tabletop RPG Gaming / DnD Greeting Card / A6': 'Natural 20 Card',
    'DnD Birthday Card/ DnD Valentines Card / RPG Birthday Card / Tabletop RPG Gaming / For Him, For Her, Boyfriend, Girlfriend, A6': 'Natural 20 Card',
    'DnD Christmas Card/ D&D Card / Dungeon Master Card / D20 / Natural 20 / Christmas Card / Tabletop RPG Gaming / DnD Greeting Card / A6': 'Christmas Card',
    'DnD Christmas Card Bundle! / D&D Card / D20 / Natural 20 / Tabletop RPG Gaming / DnD Greeting Card / Dungeons and Dragons Christmas Card A6': 'Christmas Card Bundle', 
    'DnD Birthday Card/ DnD Greeting Card / RPG Birthday Card / Tabletop RPG Gaming / For Him, For Her, Boyfriend, Girlfriend, A6': 'Mimic Card', 
    'DnD Greeting Card/ D&D Card / DnD Birthday Card / Nerdy Love / Gelatinous Cube / Engulf / Hugs / Tabletop RPG Gaming / For Him, For Her / A6': 'Gelatinous Cube Card', 
    'DnD Birthday Card/ D&D Card / Nerdy Love / Lich / Tabletop RPG Gaming / DnD Anniversary / A6': 'Lich Card', 
    'DnD Anniversary Card/ D&D Card / DnD Love / Nerdy Love / You Put the Romance in Necromancer / Tabletop RPG Gaming / A6': 'Necromancer Card',
    'Shiba Inu Birthday Card/ Dog Card / Puppy Card / Shiba Inu / Puppy / Puppy Birthday Card / Shiba Inu Birthday Card / Dog / Dog Birthday / A6': 'Shiba Birthday Card',
    'DnD Anniversary Card/ D&D Card / DnD Love / Nerdy Love / You Put the Romance in Necromancer / Tabletop RPG Gaming / A6': 'Necromancer Card',
    'Shiba Inu Get Well Soon Card/ Dog Card / Puppy Card / Shiba Inu / Puppy / Puppy Greeting Card / Shiba Inu Greeting Card / A6': 'Shiba Get Well Soon Card',
    'DnD Fathers Day Card/ D&D Card / Dungeon Master Card / D20 / Natural 20 / Best Dad Ever / Tabletop RPG Gaming / DnD Greeting Card / A6': 'Fathers Day Card',
    'DnD Birthday Card / RPG Birthday Card / Tabletop RPG Gaming / D&D Birthday Card / Funny DnD / For Him, For Her, Boyfriend, Girlfriend, A6': 'Mithril Diapers Card',
    'DnD Anniversary Card / D&D Card / Fantasy Card / Wizard Card / Nerdy Love / Cute Wizard / Tabletop RPG Gaming / A6': 'Wand Card',
    'DnD Valentine’s Day Card/ D&D Card / Nerdy Love / Cute Wizard / Want in Your Pocket / Tabletop RPG Gaming': 'Wand Card',
    'DnD Valentine’s Day Card/ D&D Card / Nerdy Love / D20 / Natural 20 / Tabletop RPG Gaming': 'Natural 20 Card',
    'DnD Valentine’s Day Card/ D&D Card / Nerdy Love / Gelatinous Cube / Engulf / Hugs / Tabletop RPG Gaming': 'Gelatinous Cube Card',
    'DnD Valentine’s Day Card/ D&D Card / Nerdy Love / Lich - Our Love Never Dies! / Tabletop RPG Gaming': 'Lich Card',
    'DnD Valentine’s Day Card/ D&D Card / Nerdy Love / You Put the Romance in Necromancer / Tabletop RPG Gaming': 'Necromancer Card'
    }

df_clean['Item Name'] = df_clean['Item Name'].map(clean_descriptions)

df_clean['Buyer User ID'] = df_clean['Buyer User ID'].replace(np.nan, 0)
df_clean['Has Account'] = df_clean['Buyer User ID'].apply(lambda x: x if x == 0 else 1)

df_cleaner = df_clean.drop(['Buyer User ID', 'Full Name', 'First Name', 'Buyer'], axis=1)

df_cleaner.to_csv('eda_data.csv')