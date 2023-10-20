import plotly.graph_objects as go
from dash import dcc
from dash import html

import pandas as pd
import numpy as np
from sentiment import sentiment
import plotly.express as px

feed = pd.read_csv('data/feedback.csv')
temp = pd.DataFrame(feed.groupby('time')['sent_value'].sum())
temp.index.name = ''
temp = temp.reset_index()
temp.columns = ['time', 'sent_value']
sentiment = px.line(x=temp['time'], y=temp['sent_value'], labels={
                    "x": "Year", "y": "Afinn score", })
sentiment.update_layout(template='plotly_white', height=400, margin={
                        "r": 150, "t": 20, "l": 150, "b": 110},)
del temp

map = px.scatter_mapbox(
    feed,
    lat="lat",
    lon="long",
    color="sentiment",
    size=[1 for i in range(feed.shape[0])],
    hover_name="feedback",
    hover_data=["sentiment", "score", "feedback"],
)

map.layout.update(
    margin={"r": 150, "t": 70, "l": 150, "b": 70},
    height=550,
    coloraxis_showscale=False,
    mapbox_style='stamen-toner',
    mapbox=dict(center=dict(lat=1.352083, lon=103.819836), zoom=10),
)

pos = 0
for i in feed['sentiment']:
    if i == 'positive':
        pos += 1
positive = pos/feed['sentiment'].shape[0]*100
negative = 100 - pos/feed['sentiment'].shape[0]*100

np = go.Figure()
np.add_trace(go.Indicator(
    mode="number",
    value=positive,
    title={
        "text": "Positive<br><span style='font-size:0.8em;color:gray'>(in percentage)</span><br>"},
    domain={'x': [0, 0.5], 'y': [0.1, 0.5]}))

np.add_trace(go.Indicator(
    mode="number",
    value=negative,
    title={
        "text": "Negative<br><span style='font-size:0.8em;color:gray'>(in percentage)</span><br>"},
    domain={'x': [0.5, 1], 'y': [0.1, 0.5]}))

del feed
layout = html.Div(children=[
    html.H4(children='Feedback'),
    html.Div(children='''Review customers experience with product'''),
    dcc.Graph(id='example-np', figure=np),
    html.H4(children='''Customers Sentiment Score'''),
    dcc.Graph(id='example-sentiment', figure=sentiment),
    html.H4(children='''Customers Feedback Location'''),
    dcc.Graph(id='example-map', figure=map), ],
    style={'color': 'blue', 'textAlign': 'center', 'paddingTop': '20px'})