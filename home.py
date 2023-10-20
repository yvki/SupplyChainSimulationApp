import plotly.graph_objects as go
from dash import dcc
from dash import html

import pandas as pd
product = pd.read_csv('data/product.csv')
validation = pd.read_csv('data/validation.csv')

import datetime
product_not_expired_count = sum([1 for i in product.id if int(datetime.datetime.now() < pd.to_datetime(product[product['id'] == i]['doe']))])

unexpired = round((product_not_expired_count/len(product))*100)
expired = 100 - unexpired

fig = go.Figure()
fig.add_trace(go.Indicator(
    mode = "number",
    value = unexpired,
    title = {"text": "Unexpired Products<br><span style='font-size:0.8em;color:gray'>(in percentage)</span><br>"},
    domain = {'x': [0, 0.5], 'y': [0.1, 0.5]}))

fig.add_trace(go.Indicator(
    mode = "number",
    value = expired,
    title = {"text": "Expired Products<br><span style='font-size:0.8em;color:gray'>(in percentage)</span><br>"},
    domain = {'x': [0.5, 1], 'y': [0.1, 0.5]}))

import plotly.express as px
map = px.scatter_mapbox(
        validation,
        lat="lat",
        lon="long",
        size=[1 for i in range(validation.shape[0])],
    )

map.layout.update(
        margin={"r": 150, "t": 70, "l": 150, "b": 70},
        height=550,
        coloraxis_showscale=False,
        mapbox_style='stamen-toner',
        mapbox=dict(center=dict(lat=1.352083, lon=103.819836), zoom=10),
    )

layout = html.Div([ 
                    html.H4(children='Product Suppliers Locations'),
                    html.Div(children='''Review transporation routes for future deliveries'''),
                    dcc.Graph(id='map', figure=map),
                    html.H4(children='Quality of Oil and Gas Products'),
                    html.Div(children='''Review existing inventory in warehouse'''), 
                    dcc.Graph(id='dist-chart', figure=fig),
                ],
            style={'color': 'blue', 'textAlign': 'center', 'paddingTop': '20px'})