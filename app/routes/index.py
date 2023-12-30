from flask import Flask, render_template, request, Blueprint
from main import get_database_connection


index_blueprint = Blueprint('index', __name__)


@index_blueprint.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    per_page = 12
    offset = (page - 1) * 12
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * from cards LIMIT 12 OFFSET ?', (offset, ))
    data = cursor.fetchall()
    return render_template('index.html', data = data, current_page=page)

