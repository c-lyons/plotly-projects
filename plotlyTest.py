import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np
import pandas as pd

np.random.seed(42)
ran_x = np.random.randint(0, 101, 100)
ran_y = np.random.randint(0, 101, 100)

data = [go.Scatter(x=ran_x,
                    y=ran_y,
                    mode='markers',
                    marker=dict(
                        size=12,
                        color='rgb(51,204,153)',
                        symbol='pentagon',
                        line = dict(width=2)
                    ))]
layout = go.Layout(title='My Title',
                    xaxis=dict(title='My X Axis'),
                    yaxis=dict(title='My Y Axis'),
                    hovermode='closest',
                    )
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='scatter.html')