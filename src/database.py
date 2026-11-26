import sqlite3
con = sqlite3.connect('database.db')

cur = con.cursor()
def create_table():
    cur.execute("CREATE TABLE IF NOT EXISTS ingredients(name, date, quantity, unit, price)")
    con.commit()

def insert_ingredient(name, date, quantity, unit, price):
    cur.execute("INSERT INTO ingredients VALUES (?, ?, ?, ?, ?)", (name, date, quantity, unit, price))
    con.commit()

def fetch_ingredients():
    cur.execute("SELECT * FROM ingredients")
    rows = cur.fetchall()
    return rows

def update_ingredient(quantity, name):
    cur.execute("UPDATE ingredients SET quantity = quantity - ? WHERE name = ?", (quantity, name))
    con.commit()
