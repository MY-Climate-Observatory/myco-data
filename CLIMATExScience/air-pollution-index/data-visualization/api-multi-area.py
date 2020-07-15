# -*- coding: utf-8 -*-
"""
13 Jun 2020
Author: Xiandi Ooi
This is a file for exploring the data visualization.
We will be looking at comparing the API values of each area within a selected state across time. 
"""
import pandas as pd
import numpy as np
from plotly.offline import plot
import plotly.express as px

# Get the data from us
df = pd.read_csv("https://www.dropbox.com/s/u0ymg0ufne0an60/api-20200713.csv?dl=1", sep = ";")
df["API_Values"] = df["API_Values"].replace(0, np.nan)
selected_state = "Sarawak"

# Subsetting the dataframe
df_temp = df.loc[(df.State == selected_state),
                ["Datetime", "API_Values", "Area"]]

# Plot the figure
fig = px.scatter(df_temp, x = "Datetime", y = "API_Values",
                 color = "Area", opacity = 0.5)

# Some additional formatting
fig.update_traces(marker = dict(line = dict(width = 0.35,
                                        color = "black")),
                  selector = dict(mode="markers"))
fig.update_layout(title_text = "Comparing API Values across {}. Click legend for multiselection".format(selected_state))
fig.update_xaxes(title_font=dict(size=1, color = "white"))
fig.update_yaxes(title_font=dict(size=1, color = "white"))

# Plot the figure
plot(fig)
