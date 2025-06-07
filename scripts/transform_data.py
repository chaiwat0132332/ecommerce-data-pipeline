import pandas as pd
def clean_data():
	df = pd.read_csv("/Users/chaiwatyingsunton/ecommerce_data_pipeline/data/product_raw.csv")
	df["price_usd"] = df["price"]
	df["category"] = df["category"].str.title()
	df = df[["id", "title", "price_usd", "category", "rating"]]
	df.to_csv("/Users/chaiwatyingsunton/ecommerce_data_pipeline/data/products_clean.csv", index = False)
	print("Clean data saced!")

if __name__=="__main__":
	clean_data()
