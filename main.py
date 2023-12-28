from flask import Flask
import sqlite3


def get_database_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_app():
    app = Flask(__name__)
    app.secret_key = 'doomer69'  

    from app.routes.index import index_blueprint
    from app.routes.show import show_card_blueprint
    from app.routes.edit_card import edit_cards_blueprint
    
    app.register_blueprint(index_blueprint)
    app.register_blueprint(show_card_blueprint)
    app.register_blueprint(edit_cards_blueprint, url_prefix='/card')
    return app