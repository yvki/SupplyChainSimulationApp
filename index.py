from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash import dcc
from app import app
import home
import macroeconomic
import feedback

navbar = dbc.NavbarSimple(children=[
    dbc.NavItem(dbc.NavLink("Home", href="/home")),
    dbc.NavItem(dbc.NavLink("Macroeconomic", href="/macroeconomic")),
    dbc.NavItem(dbc.NavLink("Feedback", href="/feedback")), ],
    color="grey",)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/macroeconomic':
        return macroeconomic.layout
    elif pathname == '/feedback':
        return feedback.layout
    else:
        return home.layout


if __name__ == '__main__':
    app.run_server(debug=False)