import pandas as pd
import sqlite3

def load_data():
    df = pd.read_csv("/Users/chaiwatyingsunton/ecommerce_data_pipeline/data/products_clean.csv")
    conn = sqlite3.connect("/Users/chaiwatyingsunton/ecommerce_data_pipeline/db/ecommerce.db")
    df.to_sql("products", conn, if_exists="replace", index=False)
    print("Data loaded into SQLite!")
          
if __name__ == "__main__":
    load_data()          