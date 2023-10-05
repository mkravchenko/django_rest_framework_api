import requests
import random
import string
from datetime import datetime
import json

url = "http://localhost:8000/api/products/"

last_product_id = requests.get(url).json()[-1].get("id")
r = requests.delete(f"http://localhost:8000/api/products/delete/{last_product_id}")
print(r.content)
