from flask import Flask, render_template, request, jsonify, session
from pathlib import Path
import sqlite3, re
from lessons import TOPICS, EXAMPLES
app = Flask(__name__)
app.secret_key = "replace-this-with-a-random-secret"
DB = Path(__file__).with_name("academy.db")

def connect():
    con=sqlite3.connect(DB)
    con.row_factory=sqlite3.Row
    return con

def setup():
    with connect() as c:
        c.executescript("""
        CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY, name TEXT, department_id INTEGER, salary INTEGER, city TEXT);
        CREATE TABLE IF NOT EXISTS departments(id INTEGER PRIMARY KEY, name TEXT);
        CREATE TABLE IF NOT EXISTS customers(id INTEGER PRIMARY KEY, name TEXT, city TEXT);
        CREATE TABLE IF NOT EXISTS orders(id INTEGER PRIMARY KEY, customer_id INTEGER, amount REAL, status TEXT);
        CREATE TABLE IF NOT EXISTS feedback(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, kind TEXT, message TEXT, created_at TEXT DEFAULT CURRENT_TIMESTAMP);
        DELETE FROM employees; DELETE FROM departments; DELETE FROM customers; DELETE FROM orders;
        INSERT INTO departments VALUES (1,'Engineering'),(2,'Sales'),(3,'Analytics');
        INSERT INTO employees VALUES (1,'Ali',1,95000,'Karachi'),(2,'Sara',2,72000,'Lahore'),(3,'Ahmed',1,88000,'Karachi'),(4,'Zain',3,81000,'Islamabad'),(5,'Hina',2,76000,'Lahore');
        INSERT INTO customers VALUES (1,'Ayesha','Karachi'),(2,'Bilal','Lahore'),(3,'Noor','Islamabad');
        INSERT INTO orders VALUES (1,1,12000,'Delivered'),(2,2,8500,'Pending'),(3,1,4000,'Delivered'),(4,3,15000,'Shipped');
        """)
setup()

@app.route("/")
def home():
    done=session.get("done",[])
    return render_template("index.html", topics=TOPICS, done=done, progress=round(100*len(done)/len(TOPICS)))

@app.route("/lesson/<int:topic_id>")
def lesson(topic_id):
    if topic_id<0 or topic_id>=len(TOPICS): return "Lesson not found",404
    return render_template("lesson.html", topic=TOPICS[topic_id], examples=EXAMPLES[topic_id], index=topic_id, total=len(TOPICS))

@app.post("/complete/<int:topic_id>")
def complete(topic_id):
    done=session.get("done",[])
    if topic_id not in done: done.append(topic_id)
    session["done"]=done
    return jsonify(progress=round(100*len(done)/len(TOPICS)),done=done)

@app.post("/query")
def query():
    sql=request.json.get("sql","").strip()
    # Read-only guard: one statement only; only SELECT or WITH; reject dangerous/side-effect tokens.
    if not re.match(r"^(SELECT|WITH)\b",sql,re.I) or ";" in sql.rstrip(";") or re.search(r"\b(INSERT|UPDATE|DELETE|DROP|ALTER|CREATE|ATTACH|DETACH|PRAGMA|REPLACE|VACUUM|LOAD_EXTENSION)\b",sql,re.I):
        return jsonify(error="Playground sirf safe SELECT / read-only WITH queries run karta hai."),400
    try:
        with connect() as c:
            cur=c.execute(sql)
            cols=[d[0] for d in (cur.description or [])]
            rows=[list(r) for r in cur.fetchmany(200)]
        return jsonify(columns=cols,rows=rows,limited=len(rows)==200)
    except sqlite3.Error as e:
        return jsonify(error="SQL error: "+str(e)),400

@app.post("/reset")
def reset():
    setup()
    return jsonify(ok=True,message="Sample database reset ho gaya.")

@app.route("/practice")
def practice(): return render_template("practice.html")
@app.route("/quiz")
def quiz(): return render_template("quiz.html")
if __name__=="__main__":
    app.run(debug=True)
