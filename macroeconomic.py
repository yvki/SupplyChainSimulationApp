from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

singapore = pd.read_csv('data/singapore.csv')
singapore = px.line(x=singapore['year'], y=singapore.inflation,
                    labels={"x": "Year", "y": "Inflation Rate",}, title='Local Rates')
singapore.update_layout(template='simple_white', height=600, margin={
                        "r": 150, "t": 50, "l": 150, "b": 50},
                        title_text='Local Rates', title_x=0.5)

world = pd.read_csv('data/world.csv')
world = px.choropleth(world, locations="country",
                      color=world['inflation'],
                      locationmode='country names', hover_name="country",
                      animation_frame=world['year'],
                      color_continuous_scale=px.colors.sequential.matter)
world.update_layout(title_text='Worldwide Rates', title_x=0.5)

layout = html.Div([
    html.H4(children='Impact of Inflation on Oil and Gas Industry'),
    dcc.Graph(id='dist-chart', figure=singapore),
    dcc.Graph(id='map', figure=world),],
    style={'color': 'blue', 'textAlign': 'center', 'paddingTop': '20px'})