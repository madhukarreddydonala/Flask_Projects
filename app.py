from flask import Flask,request,render_template,redirect

import sqlite3

app=Flask(__name__)

# get the database 
def get_db():
    return sqlite3.connect('phonebook.db')

# home route for ('/')--> index page
@app.route("/")
def home():
    
    return render_template('index.html')

# route for conacts
# @app.route('/conacts')
# def contacts():
#     # connect=get_db
#     # cur=connect.cursor()
#     con = get_db()
#     cur = con.cursor()
#     cur.execute("select  * from contacts")
#     data=cur.fetchall()
#     con.close()
#     return render_template("contacts.html",contacts=data)
@app.route("/contacts")
def contacts():
    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM contacts")
    data = cur.fetchall()
    con.close()
    return render_template("contacts.html", contacts=data)

@app.route("/add_contact", methods=["GET", "POST"])
def add_contact():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"] 

        con = get_db()
        cur = con.cursor()
        cur.execute("INSERT INTO contacts(name, phone) VALUES (?,?)", (name, phone))
        con.commit()
        con.close()

        return redirect("/contacts")

    return render_template("add_contacts.html")

@app.route("/notes")
def notes():
    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM notes")
    data = cur.fetchall()
    con.close()
    return render_template("notes.html", notes=data)


@app.route("/add_note", methods=["GET", "POST"])
def add_note():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        con = get_db()
        cur = con.cursor()
        cur.execute("INSERT INTO notes(title, content) VALUES (?,?)", (title, content))
        con.commit()
        con.close()

        return redirect("/notes")

    return render_template("add_notes.html")

if __name__=='__main__':
    app.run(debug=True)