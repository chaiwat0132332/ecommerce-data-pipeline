# scripts/analyze.py
import sqlite3
import pandas as pd

conn = sqlite3.connect("/Users/chaiwatyingsunton/ecommerce_data_pipeline/db/ecommerce.db")
query = """
SELECT category, AVG(price_usd) AS avg_price, COUNT(*) AS total_products
FROM products
GROUP BY category
ORDER BY avg_price DESC;
"""
df = pd.read_sql(query, conn)
print(df)
