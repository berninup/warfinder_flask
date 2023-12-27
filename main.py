from flask import Flask
import sqlite3


def get_database_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_app():
    app = Flask(__name__)  

    from app.routes.index import index_blueprint
    
    app.register_blueprint(index_blueprint)
    return app