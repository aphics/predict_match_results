import dash_bootstrap_components as dbc
from dash import dcc, html


def parag_leagues(id):
    return html.P("Ligas disponibles:", id=id, className="m-2 p-2 col-6 mx-auto")


def dropdown_league(id):
    return dcc.Dropdown(
        id=id,
        value="todas",
        className="m-2 p-2 col-6 mx-auto",
        clearable=False,
    )


def parag_seasons(id):
    return html.P("Temporadas disponibles:", id=id, className="m-2 p-2 col-6 mx-auto")


def dropdown_seasons(id):
    return dcc.Dropdown(
        id=id,
        className="m-2 p-2 col-6 mx-auto",
        value="actual",
        clearable=False,
    )


def get_info_button(id):
    return dbc.Button(
        id=id,
        children="GET INFO",
        color="success",
        className="m-2 p-2 col-4 mx-auto",
    )


def update_info_button(id):
    return dbc.Button(
        id=id,
        children="CREATE DATAFRAMES",
        color="success",
        className="m-2 p-2 col-4 mx-auto",
    )


def text_info(id):
    return html.Pre(" ", id=id, className="m-2 p-2 mx-auto")
