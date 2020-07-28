# -*- coding: utf-8 -*-
"""
28 July 2020
Author: Xiandi Ooi

The original data source is already very clean, we are only converting the 
format of the month and years into datetime format so that it is easier to 
do visualization.

"""

import pandas as pd

def clean_data(file_name):
    df = pd.read_csv(file_name)
    
    # Converting the year and month into a datetime object
    month = {" Jan Average": "01",
             " Feb Average": "02",
             " Mar Average": "03",
             " Apr Average": "04",
             " May Average": "05",
             " Jun Average": "06",
             " Jul Average": "07",
             " Aug Average": "08",
             " Sep Average": "09",
             " Oct Average": "10",
             " Nov Average": "11",
             " Dec Average": "12"}         
    df["Month"] = df[" Statistics"].map(month)
    df[" Year"] = df[" Year"].astype(str)
    df["Datetime"] = df[[" Year", "Month"]].apply(lambda x: ".".join(x), axis=1)
    df["Datetime"] = pd.to_datetime(df["Datetime"]) #note that the default date will be the 1st
    
    # Drop off columns that do dont hold important information
    df = df.drop(columns = [" ISO3", " Year", " Statistics", " Country", "Month"]) 
    
    # Rename column
    df = df.rename(columns = {"Rainfall - (MM)":"Monthly Average Rainfall"})
    
    # Save as csv
    df.to_csv(r"filepath\rainfall.csv", index = False)
    
    return df

def main():
    file_name = r"filepath\pr_1901_2016_MYS.csv"
    clean_data(file_name)

if __name__ == "__main__":
    main()
