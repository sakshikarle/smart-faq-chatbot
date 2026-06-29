from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import json
from ai import ask_ai

app = Flask(__name__)
app.secret_key = "secret123"

# ---------------- DATABASE ----------------
def get_db():
    conn = sqlite3.connect("chatbot.db")
    conn.row_factory = sqlite3.Row
    return conn


# ---------------- CREATE TABLES ----------------
def init_db():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS chat_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        question TEXT,
        answer TEXT
    )
    """)

    conn.commit()
    conn.close()

# Create tables automatically
init_db()


# ---------------- HOME ----------------
@app.route("/")
def home():
    if "user" not in session:
        return redirect(url_for("login"))
    return redirect(url_for("chat_page"))

# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cur.fetchone()
        conn.close()

        if user:
            session["user"] = username
            return redirect(url_for("chat_page"))
        else:
            return render_template("login.html", error="Invalid login")

    return render_template("login.html")

# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        cur = conn.cursor()

        try:
            cur.execute(
                "INSERT INTO users(username, password) VALUES(?, ?)",
                (username, password)
            )
            conn.commit()
            conn.close()
            return redirect(url_for("login"))

        except sqlite3.IntegrityError:
            conn.close()
            return "Username already exists!"

    return render_template("register.html")

# ---------------- CHAT PAGE ----------------
@app.route("/chat")
def chat_page():
    if "user" not in session:
        return redirect(url_for("login"))

    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        SELECT question
        FROM chat_history
        WHERE username=?
        ORDER BY id DESC
    """, (session["user"],))

    history = cur.fetchall()
    conn.close()

    return render_template("index.html", history=history)

# ---------------- CHAT API ----------------
@app.route("/chat", methods=["POST"])
def chat_api():
    user_msg = request.form["message"].lower()

    with open("faq_data.json", "r", encoding="utf-8") as f:
        faq = json.load(f)

    # FAQ SEARCH
    for item in faq:
        if user_msg in item["question"].lower():

            conn = get_db()
            cur = conn.cursor()

            cur.execute(
                "INSERT INTO chat_history(username, question, answer) VALUES(?, ?, ?)",
                (session["user"], user_msg, item["answer"])
            )

            conn.commit()
            conn.close()

            return item["answer"]

    # AI ANSWER
    ai_answer = ask_ai(user_msg)

    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO chat_history(username, question, answer) VALUES(?, ?, ?)",
        (session["user"], user_msg, ai_answer)
    )

    conn.commit()
    conn.close()

    return ai_answer

# ---------------- ADMIN PANEL ----------------
@app.route("/admin")
def admin():
    if "user" not in session:
        return redirect(url_for("login"))

    # simple admin check (optional)
    if session["user"] != "admin":
        return "Access Denied"

    return render_template("admin.html")

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)