import pandas as pd
from sqlalchemy import create_engine

db_config = "postgresql://postgres:8484123@localhost:5432/ecommerce_star_schema"
engine = create_engine(db_config)

def run_report():
    print("--- 📊 EXECUTING BUSINESS REPORT ---")
    
    # Query the view we just created
    df_sales = pd.read_sql("SELECT * FROM vw_sales_performance", engine)
    
    print("\n💰 Top Revenue Products:")
    print(df_sales.head())
    
    # Calculate total company revenue
    total_rev = df_sales['total_revenue'].sum()
    print(f"\n✨ Total Company Revenue: ${total_rev:,.2f}")

if __name__ == "__main__":
    run_report()