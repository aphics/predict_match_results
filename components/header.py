from dash import html


def header():
    return html.Div(
        [html.H1("PREDICTION MATCH RESULTS", className="fw-bold text-secondary")],
        className="p-2 m-1 text-center",
    )
