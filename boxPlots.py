import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np

df = pd.read_csv('data/abalone.txt')

a = np.random.choice(df['Rings'], 120, replace=False)
b = np.random.choice(df['Rings'], 100, replace=False)

data = [go.Box(y=a, name='A'), go.Box(y=b, name='B')]

layout = go.Layout(title='Abalone Box Plots')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
