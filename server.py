from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'full_friends')
app.secret_key = "pffffffff"


@app.route('/')
def index():
    users = mysql.query_db("SELECT id, name, age, DATE_FORMAT(friend_since, '%b %D, %Y') AS friend_since FROM friendlies")
    return render_template('index.html', users=users)

@app.route('/process', methods=['POST'])
def add():
    query = "INSERT INTO friendlies (name, age, friend_since) VALUES (:name, :age, NOW())"
    data = {
        'name' : request.form['name'],
        'age' : request.form['age']
    }
    friends = mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)