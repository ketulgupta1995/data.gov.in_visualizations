
import data_ops
import plotly.plotly as py

import plotly
import plotly.graph_objs as go
from plotly.graph_objs import Scatter, Layout

# import cufflinks as cf
df=data_ops.make_data_frame()


# print(df.columns)
df[data_ops.col_list[1:]]=df[data_ops.col_list[1:]].apply(data_ops.pd.to_numeric, args=('ignore',))
print(data_ops.pd.isnull(df[data_ops.col_list[1]]))
print(df[data_ops.col_list[1]].tolist())
print(df.info())


data = [
    go.Bar(
        x=df[data_ops.col_list[0]], # assign x as the dataframe column 'x'
        y=df[i]
    )
    for i in data_ops.Killed_cols
]
layout = go.Layout(
    title='Plot Title',
    xaxis=dict(
        title='x Axis',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='y Axis',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
    ,barmode='stack'
)
# layout = go.Layout(
#     barmode='stack',
#     title='Stacked Bar with Pandas'
#
# )
fig = go.Figure(data=data, layout=layout)

url = plotly.offline.plot(data, filename='pandas-bar-chart')
print (url)
