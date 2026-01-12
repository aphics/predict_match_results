# from callbacks import register_callbacks
from callbacks.callbacks_train import register_train_callbacks
from callbacks.callbacks_update_info import register_update_info_callbacks
from layouts.main_layout import main_layout

from app import app

app.layout = main_layout()

register_update_info_callbacks(app)
register_train_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True)
