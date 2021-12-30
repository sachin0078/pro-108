import csv
import pandas as pd
import plotly.figure_factory as ff
import random

df=pd.read_csv("mobBrn.csv")

data=df["Avg Rating"].tolist()
fig=ff.create_distplot([data],["avg rating"])
fig.show()