# -*- coding: utf-8 -*-
"""
13 July 2020
Author: Xiandi Ooi

Dataset version update 03
 
Adding newly released datasets.

"""

import pandas as pd

# Adding the new datasets released in June 2020
df = pd.read_csv(r"filepath\Aggregate-API.csv", sep = ";")
df1 = pd.read_csv(r"filepath\API_Melaka_2019_cleaned.csv")
df2 = pd.read_csv(r"filepath\API_NS_2019_cleaned.csv")
df3 = pd.read_csv(r"filepath\API_Pahang_2019_cleaned.csv")
df4 = pd.read_csv(r"filepath\API_Penang_2019_cleaned.csv")
df5 = pd.read_csv(r"filepath\API_Perak_2019_cleaned.csv")
df6 = pd.read_csv(r"filepath\API_Perlis_2019_cleaned.csv")
df7 = pd.read_csv(r"filepath\API_Sabah_2019_cleaned.csv")
df8 = pd.read_csv(r"filepath\API_Sarawak_2019_cleaned.csv")
df9 = pd.read_csv(r"filepath\API_Terengganu_2019_cleaned.csv")

df_total = pd.concat([df, df1, df2, df3, df4, df5, df6, df7, df8, df9])
df_total = df_total.drop(columns = ["Unnamed: 0"])

# Making sure our df won't have the column "Unnamed:0" when we load it again
# Also changing the way we name the dataset to reflect changes
df_total.to_csv(r"filepath\api-20200713.csv", sep = ";", index = False)
