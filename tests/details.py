import requests


r = requests.get("http://localhost:8000/api/products/3")
print(r.content)