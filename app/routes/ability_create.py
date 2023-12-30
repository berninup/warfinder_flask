from flask import Flask, render_template, flash, request, Blueprint, url_for, redirect
from app.models.ability_model import Ability
from main import get_database_connection

create_ability_blueprint = Blueprint('create_ability', __name__)

@create_ability_blueprint.route('/ability/create', methods=['GET', 'POST'])
def create_ability():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        level = request.form['level']
        
        try:
            ability = Ability(name, description, level)
            conn = get_database_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO abilities (name, description, level) VALUES (?,?,?)', (name, description, level))
            conn.commit()
            if ability.alt_description != ability.description:
                conn = get_database_connection()
                cursor = conn.cursor()
                cursor.execute('INSERT INTO abilities (name, description, level) VALUES (?,?,?)', (ability.alt_name, ability.alt_description, level))
                conn.commit()
                flash('Alt ability created', 'success')
            flash('Ability created.', 'success')     
            return redirect(url_for('index.home'))
        except ValueError as error:
            flash(str(error))
            
    levels = Ability.ABILITY_LEVELS
    return render_template('add_ability.html', levels = levels)          