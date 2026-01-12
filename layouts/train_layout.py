import dash_bootstrap_components as dbc
from callbacks.utilities_train import get_leagues
from components.components_train import dropdown_league, parag_leagues
from components.loading import loading
from dash import html


def train_content():
    return dbc.Card(
        [
            html.Div(
                [
                    parag_leagues("leagues"),
                    dropdown_league("dropdown_leagues_train"),
                ],
                className="border rounded m-2 p-2 col-10 mx-auto shadow-sm",
            ),
        ]
    )
