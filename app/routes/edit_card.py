from flask import Flask, render_template, request, redirect, url_for, Blueprint, flash
from main import get_database_connection

edit_cards_blueprint = Blueprint('edit_card', __name__)

@edit_cards_blueprint.route('/edit/<card_name>', methods=['GET'])
def show_edit_card_form(card_name):
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cards WHERE name = ?', (card_name,))
    card = cursor.fetchone()
    if card is None:
        flash('Card not found.', 'error')
        return redirect(url_for('index'))
    return render_template('edit_card.html', card=card)

@edit_cards_blueprint.route('/edit/<card_name>', methods=['POST'])
def edit_card_name(card_name):
    new_name = request.form['card_name']
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE cards SET name = ? WHERE name = ?', (new_name, card_name))
    conn.commit()
    flash('Card name updated successfully.', 'success')
    return redirect(url_for('show_card.card_show', card_name=new_name))