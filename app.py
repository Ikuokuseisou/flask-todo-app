from flask import Flask,render_template,request,redirect,url_for
import sqlite3
app = Flask(__name__)

@app.route("/")
def home():

    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS todos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   task TEXT
                   )
                   """)

    cursor.execute("SELECT * FROM todos")
    tasks = cursor.fetchall()

    return render_template("index.html", tasks = tasks) 

@app.route("/add",methods = ["POST"])
def add():
    task = request.form.get("task")

    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO todos (task) VALUES (?)",
        (task,)
    )

    conn.commit()

    return redirect(url_for("home"))

@app.route("/delete/<int:id>")
def delete():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM todos WHERE id = ?",(id,))
    conn,commit()

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)