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
    database.insert_ingredient(name.strip().lower(), date, quantity, unit.strip().upper(), price)

def use_ingredient():
    name = input("\nEnter ingredient name: ")
    check = database.check_ingredient(name.strip().lower())
    if check is None:
        print("Ingredient not found!")
        return
    while True:
        try:
            quantity = float(input("Enter quantity used: "))
            available = check[2]
            if quantity > available:
                print("\nIngredients not enough!!\n")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter numeric values for quantity")
    updated = database.update_ingredient(quantity, name.strip().lower())
    if updated == 0:
        print("\nNothing has changed.")
    else:
        print("\nList updated!")

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