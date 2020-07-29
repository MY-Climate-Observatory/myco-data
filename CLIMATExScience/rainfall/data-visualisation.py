# -*- coding: utf-8 -*-
"""
28 July 2020
Author: Xiandi Ooi

Simple visuals segmented into two selection, month and year

"""
import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot

def by_year(selected_year, df):
    """
    Input: Year value
    Output: Line plot of average rainfall in the selected year
    """
    df_temp = df[df.index.year == selected_year]
    
    #initiate the figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(x = list(df_temp.index), 
                             y = list(df_temp["Monthly Average Rainfall"])))
    fig.update_layout(title_text = "Monthly Average Rainfall in {}".format(selected_year))
    plot(fig)
    return fig


def by_month(selected_month, df):
    """
    Input: Month value
    Output: Line plot of average rainfall in the month across different years
    """    
    months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
              "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
    
    month_value = months.get(selected_month)
    
    df_temp = df[df.index.month == month_value]
    
    #initiate the figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(x = list(df_temp.index), 
                             y = list(df_temp["Monthly Average Rainfall"])))
    fig.update_layout(title_text = "Average Rainfall in {} from 1901-2016".format(selected_month))
    plot(fig)
    return fig

def main():
    df = pd.read_csv(r"filepath\rainfall.csv")
    df.index = pd.DatetimeIndex(df["Datetime"])
    # Imagine that there is a code to choose between either one here
    selected_year = 2016
    selected_month = "January"
    by_year(selected_year)
    by_month(selected_month)

if __name__ == "__main__":
    main()
