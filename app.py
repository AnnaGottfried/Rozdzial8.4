from flask import Flask,render_template,request,redirect,url_for
import pdb

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html", Nazwa="Kontakt", strona="/kontakt")

@app.route('/kontakt',methods=['GET','POST'])
def kontakt():
    if request.method == "POST":
        print("form data:")
        print('message:{}'.format(request.form.get('message')))
        wiadomosc=request.form.get('message')
      #  return redirect("/podziekowania",message=wiadomosc)
        return render_template("podziekowania.html", message=wiadomosc)

    elif request.method == "GET":
        return render_template("kontakt.html", Nazwa="Strona główna", strona="/")

@app.route('/podziekowania',methods=['GET','POST'])
def dziekuje():
    wiadomosc = request.form.get('message')
    imie= request.form.get('imie')
    nazwisko= request.form.get('nazwisko')
    return render_template("podziekowania.html", message=wiadomosc, imie=imie,nazwisko=nazwisko, Nazwa="Strona główna", strona="/")
'''

       print("We received P'OST")
        print(request.form)
        return redirect("/")
    elif request.method == 'GET':
        return render_template("kontakt.html")


@app.route('/message', methods=['GET', 'POST'])
def message():
   if request.method == 'GET':
       print("We received GET")
       return render_template("form.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")'''