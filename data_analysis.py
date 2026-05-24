import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect database
conn = sqlite3.connect("food_delivery.db")

# Load orders table
orders_df = pd.read_sql_query("SELECT * FROM orders", conn)

# Show orders
print(orders_df)

# Total sales
total_sales = orders_df["total"].sum()
print("\nTotal Sales:", total_sales)

# Restaurant-wise sales
restaurant_sales = orders_df.groupby("restaurant_id")["total"].sum()

print("\nRestaurant Wise Sales:")
print(restaurant_sales)

# Plot graph
restaurant_sales.plot(kind="bar")

plt.title("Restaurant Sales")
plt.xlabel("Restaurant ID")
plt.ylabel("Total Sales")

plt.show()