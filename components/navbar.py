import dash_bootstrap_components as dbc
from layouts.get_info_layout import update_info_content
from layouts.train_layout import train_content

tab3_content = dbc.Card([dbc.CardHeader()])


def navbar():
    tab_update_info = dbc.Tab(
        update_info_content(), label="UPDATE INFO", className="mx-auto"
    )
    tab_train = dbc.Tab(train_content(), label="TRAIN", className="mx-auto")
    # tab_predict = dbc.Tab(train_content(), label="PREDICT", className="mx-auto")
    return dbc.Tabs(
        [
            tab_update_info,
            tab_train,
            # tab_predict
            dbc.Tab(tab3_content, label="PREDICT"),
        ],
        className="m-2",
    )
