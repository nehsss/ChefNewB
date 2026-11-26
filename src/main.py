import database

database.create_table()
#database.insert_ingredient('Tomato', '2023-06-01', 10, 'kg', 20.0)

def add_ingredient():
    while True:
        try:
            name = input("Enter ingredient name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            quantity = float(input("Enter quantity: "))
            unit = input("Enter unit: ")
            price = float(input("Enter price: "))
            break
        except ValueError:
            print("Invalid input. Please enter numeric values for quantity and price.")
    database.insert_ingredient(name, date, quantity, unit, price)

def use_ingredient():
    while True:
        try:
            name = input("Enter ingredient name: ")
            quantity = float(input("Enter quantity used: "))
            break
        except ValueError:
            print("Invalid input. Please enter numeric values for quantity")
    database.update_ingredient(quantity, name)
while True:
    print("\n1. Add Ingredient")
    print("2. View Ingredients")
    print("3. Use Ingredient")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_ingredient()
    elif choice == '2':
        ingredients = database.fetch_ingredients()
        for ingredient in ingredients:
            print(ingredient)
    elif choice == '3':
        use_ingredient()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")