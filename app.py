from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT,
            email TEXT,
            mobile TEXT,
            subject TEXT,
            message TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/achievements")
def achievements():
    return render_template("achievements.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")



@app.route("/contact", methods=["POST"])
def contact():
    full_name = request.form["full_name"]
    email = request.form["email"]
    mobile = request.form["mobile"]
    subject = request.form["subject"]
    message = request.form["message"]

    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (full_name, email, mobile, subject, message) VALUES (?, ?, ?, ?, ?)",
                   (full_name, email, mobile, subject, message))
    conn.commit()
    conn.close()

    return "Thank you for contacting me!"

@app.route('/admin/messages')
def admin_messages():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contacts')
    messages = cursor.fetchall()
    conn.close()
    return render_template('messages.html', messages=messages)




if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5010)





