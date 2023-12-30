from flask import Flask, render_template, request, Blueprint, abort
from main import get_database_connection

show_ability_blueprint = Blueprint('show_ability', __name__)

@show_ability_blueprint.route('/ability/<ability_name>')
def ability_show(ability_name):
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM abilities WHERE name = ?', (ability_name,))
    ability = cursor.fetchone()
    
    if ability is None:
        abort(404)
        
    return render_template('ability_detail.html', ability=ability)