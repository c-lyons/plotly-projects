import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np

df = pd.read_csv('data/auto-mpg.csv')

data = [go.Histogram(x=df['mpg'],
                    xbins=dict(start=0,
                                end=100,
                                size=2),
                    histnorm='percent',
                    marker_color='#EB89B5',
                    opacity=0.75)]

layout = go.Layout(title='Histogram of MPG')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='mpg.html')
