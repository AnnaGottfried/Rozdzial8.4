from flask import Flask, render_template,url_for, redirect,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return "hello this is my first page <h1> Hello </h1>"

@app.route('/nowa', methods=["POST","GET"])
def user(name, nazwisko):
    if request.method == "GET":
        return f'hello {name} {nazwisko}'

@app.route('/admin')
def admin():
    return redirect(url_for('user', name ='Admin!'))

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        User = request.form['imie']
        lastname = request.form['nazwisko']
        return redirect(url_for('user', name=User, nazwisko=lastname))

    elif request.method == "GET":
        return render_template('login.html')