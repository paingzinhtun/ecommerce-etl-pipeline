import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Set seed for reproducibility
np.random.seed(42)

def generate_messy_data():
    # 1. Products - All columns now have exactly 11 rows
    products = pd.DataFrame({
        'product_id': range(1, 12),
        'sku': [f"SKU-{100+i}" for i in range(10)] + ["SKU-101"], # 11 items
        'name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'USB Cable', 
                 'Phone', 'Tablet', 'Webcam', 'Headset', 'Desk Lamp', 'Old Mouse'], # 11 items
        'category': ['Electronics', 'Electronics', 'Electronics', None, 'Accessories', 
                     'electronics', 'Electronics', 'Electronics', 'Audio', 'Office', 'Electronics'], # 11 items
        'unit_cost': [800, 20, 45, 150, 5, 500, 300, 40, 60, 25, 15], # 11 items
        'unit_price': [1200, 35, 75, 250, 15, 800, 450, 80, 110, 45, 25] # 11 items
    })

    # 2. Customers - All columns have 5 rows
    cities = ["Yangon", "YANGON", " yangon ", "Mandalay", "mandalay", "Naypyidaw"]
    customers = pd.DataFrame({
        'customer_id': range(1, 6),
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'city': [random.choice(cities) for _ in range(5)],
        'created_at': [datetime(2023, 1, 1) + timedelta(days=x) for x in range(5)]
    })

    # 3. Orders - All columns have 5 rows
    orders = pd.DataFrame({
        'order_id': [1001, 1002, 1003, 1004, 1005],
        'customer_id': [1, 2, 1, 4, 3],
        'order_date': ['2023-10-01', '2023-10-01', '2023-10-02', 'invalid_date', '2023-10-03'],
        'payment_method': ['Credit Card', 'Cash', 'Credit Card', 'PayPal', 'Cash']
    })

    # 4. Order Items - All columns have 6 rows
    order_items = pd.DataFrame({
        'order_id': [1001, 1001, 1002, 1003, 1004, 1005],
        'product_id': [1, 2, 3, 1, 5, 2],
        'quantity': [1, 2, -1, 1, 10, 1], 
        'item_price': [1200, 35, 75, 1200, 15, 35]
    })

    # 5. Inventory Snapshots - All columns have 10 rows
    inventory = pd.DataFrame({
        'snapshot_date': ['2023-10-01'] * 10,
        'product_id': range(1, 11),
        'on_hand': [5, 50, 30, 10, 100, 8, 15, 20, 12, 40]
    })

    # Save to CSVs
    products.to_csv('products.csv', index=False)
    customers.to_csv('customers.csv', index=False)
    orders.to_csv('orders.csv', index=False)
    order_items.to_csv('order_items.csv', index=False)
    inventory.to_csv('inventory_snapshots.csv', index=False)
    
    print("✅ Success: 5 messy CSV files generated.")

if __name__ == "__main__":
    generate_messy_data()