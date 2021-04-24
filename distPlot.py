import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd
import numpy as np

x1 = np.random.randn(1000)
x2 = np.random.randn(1000)-1
x3 = np.random.randn(1000)-0.5
x4 = np.random.randn(1000)+3

hist_data = [x1, x2, x3, x4]
group_labels = ['X1', 'X2', 'X3', 'X4']

fig = ff.create_distplot(hist_data, group_labels, bin_size=0.5)

pyo.plot(fig, filename='histPlot.html')