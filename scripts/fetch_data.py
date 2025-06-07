import requests
import pandas as pd

def fetch_products():
	url = "http://fakestoreapi.com/products"
	response = requests.get(url)
	data = response.json()
	df = pd.DataFrame(data)
	df.to_csv("data/product_raw.csv", index = False)
	print("Data saved!")
if __name__== "__main__":
	fetch_products()
