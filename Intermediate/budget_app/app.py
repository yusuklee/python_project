from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app=Flask(__name__)
DB_NAME = 'budget.db'

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                type TEXT CHECK(type IN ('income', 'expense')) NOT NULL,
                category TEXT NOT NULL,
                amount INTEGER NOT NULL
            );
        ''')

@app.route('/')
def index():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute("SELECT * FROM transactions ORDER BY date DESC")
        records = cursor.fetchall()
        total_income = sum(row[4] for row in records if row[2]=='income')
        total_expense = sum(row[4] for row in records if row[2]=='expense')
        return render_template('index.html', records=records, income = total_income, expense=total_expense)
    

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method =='POST':
        date=request.form['date']
        t_type = request.form['type']
        category = request.form['category']
        amount = int(request.form['amount'])

        with sqlite3.connect(DB_NAME) as conn:
            conn.execute('INSERT INTO transactions (date, type, category, amount) VALUES(?, ?, ?, ?)',
                        (date, t_type,category,amount))
        return redirect('/')
    return render_template('add.html')
    

if __name__ =='__main__':
    init_db()
    app.run(debug=True)