import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np

df = pd.read_csv('data/abalone.txt')
df.head()

data = [go.Histogram(x=df['Length'],
                    xbins=dict(start=df.Length.min(),
                                end=df.Length.max(),
                                size=0.05),
                    histnorm='percent',
                    marker_color='#000080',
                    opacity=0.75)]

layout = go.Layout(title='Histogram of Abalone Length')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='abaloneHistogram.html')
