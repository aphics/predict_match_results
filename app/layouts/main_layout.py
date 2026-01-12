import dash_bootstrap_components as dbc
from components.header import header
from components.navbar import navbar
from dash import Dash, dcc, html


def main_layout():
    return html.Div([header(), html.Hr(className="m-4"), navbar()])
