import database

database.create_table()
database.insert_ingredient('Tomato', '2023-06-01', 10, 'kg', 20.0)
print(database.fetch_ingredients())