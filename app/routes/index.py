from flask import Flask, render_template, request, Blueprint
from main import get_database_connection
from app.routes.ability_index import get_all_abilities


index_blueprint = Blueprint('index', __name__)


@index_blueprint.route('/')
def home():
    abilities = get_all_abilities()
    page = request.args.get('page', 1, type=int)    
    offset = (page - 1) * 12
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * from cards LIMIT 12 OFFSET ?', (offset, ))
    data = cursor.fetchall()
    return render_template('card_list.html', data = data, current_page=page, abilities=abilities)

