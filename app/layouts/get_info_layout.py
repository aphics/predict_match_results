import dash_bootstrap_components as dbc
from components.components_update_info import (
    dropdown_league,
    dropdown_seasons,
    get_info_button,
    parag_leagues,
    parag_seasons,
    text_info,
    update_info_button,
)
from components.loading import loading
from dash import html


def update_info_content():

    return dbc.Card(
        [
            html.Div(
                [
                    parag_leagues("update_leagues"),
                    dropdown_league("dropdown_league_update"),
                ],
                className="border rounded m-2 p-2 col-10 mx-auto shadow-sm",
            ),
            html.Div(
                [
                    parag_seasons("seasons"),
                    dropdown_seasons("dropdown_seasons"),
                ],
                className="border rounded m-2 p-2 col-10 mx-auto shadow-sm",
            ),
            html.Div(
                [
                    get_info_button("update_info_button"),
                    update_info_button("create_df_button"),
                ],
                className="d-flex justify-content-center",
            ),
            html.Div(
                [loading("ejecucion_proceso", text_info("text_info"))],
                className="d-flex justify-content-center",
            ),
        ]
    )
