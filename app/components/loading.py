from dash import dcc


def loading(id, children):
    return dcc.Loading(
        id=id,
        type="cube",
        style={"transform": "scale(0.3)"},
        color="#007430",
        children=children,
    )
