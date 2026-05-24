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
cursor.execute("INSERT OR IGNORE INTO restaurants (id,name) VALUES (3,'Burger Barn')")
cursor.execute("INSERT OR IGNORE INTO restaurants (id,name) VALUES (4,'Sushi Delight')")
cursor.execute("INSERT OR IGNORE INTO restaurants (id,name) VALUES (5,'Taco Fiesta')")
cursor.execute("INSERT OR IGNORE INTO restaurants (id,name) VALUES (6,'Noodle House')")
cursor.execute("INSERT OR IGNORE INTO restaurants (id,name) VALUES (7,'Salad Bar')")
cursor.execute("INSERT OR IGNORE INTO restaurants (id,name) VALUES (8,'Dessert Heaven')")
cursor.execute("INSERT OR IGNORE INTO restaurants (id,name) VALUES (9,'Chinese Wok')")
cursor.execute("INSERT OR IGNORE INTO restaurants (id,name) VALUES (10,'Biriyani Palace')")

cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (1,1,'Paneer Tikka', 249)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (2,1,'Veg Biryani', 199)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (3,1,'Butter Naan', 49)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (4,1,'Dal Makhani', 179)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (5,1,'Masala Dosa', 129)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (6,2,'Margherita Pizza',299)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (7,2,'Farmhouse Pizza',399)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (8,2,'Cheese Garlic Bread',149)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (9,2,'Veg Pasta',199)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (10,2,'Chocolate Lava Cake',129)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (11,3,'Chicken Burger',149)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (12,3,'Veg Burger',129)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (13,3,'French Fries',99)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (14,3,'Cheese Burger',179)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (15,3,'Cold Coffee',89)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (16,4,'California Roll',349)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (17,4,'Salmon Sushi',499)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (18,4,'Miso Soup',149)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (19,4,'Tempura Prawns',399)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (20,4,'Green Tea',99)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (21,5,'Chicken Taco',199)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (22,5,'Veg Taco',169)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (23,5,'Nachos',149)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (24,5,'Mexican Burrito',249)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (25,5,'Churros',129)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (26,6,'Hakka Noodles',199)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (27,6,'Manchurian',179)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (28,6,'Spring Rolls',149)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (29,6,'Fried Rice',189)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (30,6,'Chilli Paneer',229)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (31,7,'Caesar Salad',179)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (32,7,'Greek Salad',199)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (33,7,'Fruit Salad',149)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (34,7,'Paneer Salad',229)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (35,7,'Veggie Bowl',189)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (36,8,'Chocolate Brownie',149)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (37,8,'Vanilla Ice Cream',99)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (38,8,'Red Velvet Cake',249)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (39,8,'Chocolate Sundae',199)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (40,8,'Blueberry Cheesecake',299)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (41,9,'Veg Hakka Noodles',199)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (42,9,'Chicken Fried Rice',249)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (43,9,'Chilli Chicken',299)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (44,9,'Veg Manchurian',189)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (45,9,'Spring Rolls',149)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (46,10,'Chicken Biryani',299)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (47,10,'Veg Biryani',249)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (48,10,'Mutton Biryani',399)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (49,10,'Raita',49)")
cursor.execute("INSERT OR IGNORE INTO menu_items (id,restaurant_id,item_name,price) VALUES (50,10,'Gulab Jamun',99)")

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