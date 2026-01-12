from callbacks.utilities_update_info import (
    build_dfs_with_prev_info_seasons,
    dicto_leagues,
    dicto_seasons,
    get_seasons_info,
)
from dash import Input, Output, State


def register_update_info_callbacks(app):

    # LOAD LEAGUES
    @app.callback(
        Output("dropdown_league_update", "options"),
        Input("dropdown_league_update", "id"),
    )
    def load_leagues(_):
        visual_options = [dict(label="TODAS", value="todas")] + [
            {"label": row.upper(), "value": row} for row in dicto_leagues().keys()
        ]
        return visual_options

    # LOAD SEASONS
    @app.callback(
        Output("dropdown_seasons", "options"), Input("dropdown_seasons", "id")
    )
    def load_seasons(_):
        return [{"label": row.upper(), "value": row} for row in dicto_seasons().keys()]

    # GET INFO
    @app.callback(
        Output("text_info", "children", allow_duplicate=True),
        Input("update_info_button", "n_clicks"),
        State("dropdown_league_update", "value"),
        State("dropdown_seasons", "value"),
        prevent_initial_call=True,
    )
    def get_info(n_clicks, league_value, seasons_value):
        msj = []
        if n_clicks and n_clicks > 0:
            if seasons_value == "actual":
                if league_value == "todas":
                    for league in dicto_leagues().keys():
                        result = get_seasons_info(
                            league, dicto_leagues()[league][1], current=True
                        )
                        msj.append(result)
                else:
                    result = get_seasons_info(
                        league_value, dicto_leagues()[league_value][1], current=True
                    )
                    msj.append(result)
            else:
                if league_value == "todas":
                    for league in dicto_leagues().keys():
                        result = get_seasons_info(
                            league, dicto_leagues()[league][1], current=False
                        )
                        msj.append(result)
                else:
                    result = get_seasons_info(
                        league_value, dicto_leagues()[league_value][1], current=False
                    )
                    msj.append(result)
        return "\n".join(msj)

    # CREATE DATAFRAMES
    @app.callback(
        Output("text_info", "children", allow_duplicate=True),
        Input("create_df_button", "n_clicks"),
        State("dropdown_league_update", "value"),
        prevent_initial_call=True,
    )
    def create_dataframes(n_clicks, league_value):
        msj = []
        if n_clicks and n_clicks > 0:
            if league_value == "todas":
                for league in dicto_leagues().keys():
                    result = build_dfs_with_prev_info_seasons(league)
                    msj.append(result)
            else:
                result = build_dfs_with_prev_info_seasons(league_value)
                msj.append(result)
        return "\n".join(msj)
