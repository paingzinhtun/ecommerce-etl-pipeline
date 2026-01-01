import pandas as pd
from sqlalchemy import create_engine

# 1. Database Connection Configuration
# Format: postgresql://username:password@localhost:5432/database_name
db_config = "postgresql://postgres:8484123@localhost:5432/ecommerce_star_schema"
engine = create_engine(db_config)

def load_to_postgres():
    try:
        # Load Cleaned CSVs into DataFrames
        df_products = pd.read_csv('data_clean/products_clean.csv')
        df_customers = pd.read_csv('data_clean/customers_clean.csv')
        df_order_items = pd.read_csv('data_clean/order_items_clean.csv')

        print("🚀 Starting Database Load...")

        # 2. Load Dimensions First (Crucial because of Foreign Keys)
        # if_exists='append' adds data to existing tables
        df_customers.to_sql('dim_customers', engine, if_exists='append', index=False)
        print("✅ dim_customers loaded.")

        # Note: We only need columns that match our SQL schema for products
        # We drop 'unit_cost' and 'category' if they aren't in our dim_products table
        df_products[['product_id', 'sku', 'name', 'category', 'unit_price']].to_sql(
            'dim_products', engine, if_exists='append', index=False
        )
        print("✅ dim_products loaded.")

        # 3. Load Facts Last
        df_order_items.to_sql('fact_order_items', engine, if_exists='append', index=False)
        print("✅ fact_order_items loaded.")

        print("\n🏆 ETL Pipeline Completed Successfully!")

    except Exception as e:
        print(f"❌ Error during load: {e}")

if __name__ == "__main__":
    load_to_postgres()