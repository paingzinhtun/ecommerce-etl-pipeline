import pandas as pd
import os

os.makedirs('data_clean', exist_ok=True)

def clean_data():
    # --- CLEAN PRODUCTS ---
    df_p = pd.read_csv('data_raw/products.csv')
    # Fix: Remove duplicate SKUs (keeping first)
    df_p = df_p.drop_duplicates(subset=['sku'], keep='first')
    # Fix: Fill missing category and capitalize
    df_p['category'] = df_p['category'].fillna('Unknown').str.capitalize()
    df_p.to_csv('data_clean/products_clean.csv', index=False)

    # --- CLEAN CUSTOMERS ---
    df_c = pd.read_csv('data_raw/customers.csv')
    # Fix: Strip spaces and standardize city names
    df_c['city'] = df_c['city'].str.strip().str.title()
    df_c.to_csv('data_clean/customers_clean.csv', index=False)

    # --- CLEAN ORDER ITEMS ---
    df_oi = pd.read_csv('data_raw/order_items.csv')
    # Fix: Remove negative quantities
    df_oi = df_oi[df_oi['quantity'] > 0]
    df_oi.to_csv('data_clean/order_items_clean.csv', index=False)

    print("✅ Step 2: Clean data saved in /data_clean")

if __name__ == "__main__":
    clean_data()