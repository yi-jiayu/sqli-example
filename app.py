from flask import Flask, request, render_template

import db

db.init_db()
app = Flask(__name__)


def login(username, password):
    conn = db.connect()
    query = db.build_query(username, password)

    print('Running query:', query)

    c = conn.cursor()
    c.execute(query)
    row = c.fetchone()

    print('Result:', row)

    conn.close()

    if row is not None:
        return row[0]
    else:
        return None


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def dashboard():
    username, password = request.form['username'], request.form['password']
    username = login(username, password)

    if username:
        return render_template('dashboard.html', username=username)
    else:
        return render_template('index.html', message='Login failed!')
