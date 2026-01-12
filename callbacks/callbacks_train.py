from callbacks.utilities_train import get_leagues
from dash import Input, Output, State


def register_train_callbacks(app):

    # LOAD LEAGUES
    @app.callback(
        Output("dropdown_leagues_train", "options"),
        Output("dropdown_leagues_train", "value"),
        Input("dropdown_leagues_train", "id"),
    )
    def load_leagues(_):
        leagues = get_leagues()
        visual_options = [{"label": row.upper(), "value": row} for row in leagues]
        first_value = visual_options[0]["value"]
        return visual_options, first_value
