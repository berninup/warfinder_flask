from flask import Flask, render_template, request, Blueprint, abort
from main import get_database_connection

show_card_blueprint = Blueprint('show_card', __name__)

@show_card_blueprint.route('/card/<card_name>')
def card_show(card_name):
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cards WHERE name = ?', (card_name,))
    card = cursor.fetchone()
    
    if card is None:
        abort(404)
        
    return render_template('card_detail.html', card=card)