# food_delivery.py
# Simple Food Delivery System using Python + SQLite
# Author: (Your Name)

import sqlite3

# ---------- DATABASE SETUP ----------
conn = sqlite3.connect("food_delivery.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS restaurants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS menu_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    restaurant_id INTEGER,
    item_name TEXT NOT NULL,
    price REAL NOT NULL,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    restaurant_id INTEGER,
    total REAL,
    status TEXT DEFAULT 'PLACED',
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    menu_item_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (menu_item_id) REFERENCES menu_items(id)
)""")

conn.commit()

# ---------- SAMPLE DATA ----------
cursor.execute("INSERT OR IGNORE INTO restaurants (id,name) VALUES (1,'Spice Hub')")
cursor.execute("INSERT OR IGNORE INTO restaurants (id,name) VALUES (2,'Pizza Plaza')")

cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (1,1,'Paneer Tikka', 249)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (2,1,'Veg Biryani', 199)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (3,2,'Margherita Pizza', 299)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (4,2,'Farmhouse Pizza', 349)")

conn.commit()

# ---------- FUNCTIONS ----------
def create_user():
    name = input("Enter your name: ")
    phone = input("Enter your phone: ")
    cursor.execute("INSERT INTO users (name, phone) VALUES (?, ?)", (name, phone))
    conn.commit()
    print("User created successfully!\n")

def show_restaurants():
    cursor.execute("SELECT * FROM restaurants")
    for row in cursor.fetchall():
        print(row[0], "-", row[1])

def show_menu(restaurant_id):
    cursor.execute("SELECT id,item_name,price FROM menu_items WHERE restaurant_id=?", (restaurant_id,))
    for row in cursor.fetchall():
        print(row[0], "-", row[1], "-", "₹", row[2])

def place_order():
    user_id = int(input("Enter your user ID: "))
    show_restaurants()
    rest_id = int(input("Choose restaurant ID: "))
    show_menu(rest_id)

    order_total = 0
    cursor.execute("INSERT INTO orders (user_id, restaurant_id, total) VALUES (?, ?, ?)", (user_id, rest_id, 0))
    order_id = cursor.lastrowid

    while True:
        item_id = int(input("Enter item ID to add (0 to finish): "))
        if item_id == 0:
            break
        qty = int(input("Enter quantity: "))
        cursor.execute("SELECT price FROM menu_items WHERE id=?", (item_id,))
        price = cursor.fetchone()[0]
        order_total += price * qty
        cursor.execute("INSERT INTO order_items (order_id, menu_item_id, quantity) VALUES (?, ?, ?)",
                       (order_id, item_id, qty))

    cursor.execute("UPDATE orders SET total=? WHERE id=?", (order_total, order_id))
    conn.commit()
    print(f"Order placed! Order ID: {order_id}, Total: ₹{order_total}\n")

def show_orders(user_id):
    cursor.execute("SELECT id, total, status FROM orders WHERE user_id=?", (user_id,))
    for row in cursor.fetchall():
        print(f"Order {row[0]} | Total: ₹{row[1]} | Status: {row[2]}")

# ---------- MAIN MENU ----------
while True:
    print("\n==== FOOD DELIVERY SYSTEM ====")
    print("1. Register User")
    print("2. Show Restaurants")
    print("3. Show Menu")
    print("4. Place Order")
    print("5. Show My Orders")
    print("6. Exit")

    choice = input("Enter choice: ")
    if choice == "1":
        create_user()
    elif choice == "2":
        show_restaurants()
    elif choice == "3":
        rid = int(input("Enter restaurant ID: "))
        show_menu(rid)
    elif choice == "4":
        place_order()
    elif choice == "5":
        uid = int(input("Enter your user ID: "))
        show_orders(uid)
    elif choice == "6":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
