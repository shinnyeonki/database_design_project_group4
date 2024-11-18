from flask import Blueprint, render_template

connection = None
def enroll_connection(conn):
    global connection
    connection = conn

main = Blueprint('main', __name__)

@main.route('/')
def index(): #연결 test 및 home.html 렌더링
    return render_template('home.html')


