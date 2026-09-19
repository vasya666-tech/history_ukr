from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def next_page():
    return redirect(url_for('search'))

@app.route('/search')
def sarch_page():
    return render_template('index.html', page='search')

@app.route('/info')
def first_page():
    return render_template('index.html', page='first')

@app.route('/figures')
def second_page():
    return render_template('index.html', page='second')
