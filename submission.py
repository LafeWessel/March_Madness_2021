# -*- coding: utf-8 -*-
"""
Spyder Editor

Created by Lafe Wessel on 3/13/2021

"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# read in data
df = pd.read_excel("March Madness.xlsx",sheet_name = "2020")
df['Score'] = 0

col_of_interest = ["Wins Against Top 25 RPI Teams",
                   "Scoring Differential Per Game",
                   "ESPN Strength of Schedule"]

# scale data
for c in col_of_interest:
    df[c] = MinMaxScaler((0,1)).fit_transform(df[[c]])
#end for    

# calculate score
df.Score += df[col_of_interest[0]] * 0.75
df.Score += df[col_of_interest[1]] * 0.75
df.Score += df[col_of_interest[2]] * 0.5

# sort and print
df = df.sort_values(['Score'],ascending = False)

for i in range(10):
    print(i+1, df.iloc[i,:]['Team'])

input()