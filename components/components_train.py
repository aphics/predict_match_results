from dash import dcc, html


def parag_leagues(id):
    return html.P("Ligas disponibles:", id=id, className="m-2 p-2 col-6 mx-auto")


def dropdown_league(id):
    return dcc.Dropdown(
        id=id,
        # value="todas",
        className="m-2 p-2 col-6 mx-auto",
        clearable=False,
    )
