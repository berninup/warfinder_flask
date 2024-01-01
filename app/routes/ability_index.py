from flask import Flask, render_template, request
from main import get_database_connection



def get_all_abilities():
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * from abilities')
    abilities = cursor.fetchall()
    return abilities