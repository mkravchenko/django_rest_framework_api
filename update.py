import requests
import random
import string
from datetime import datetime
import json

data = {"title": "update", "price": random.randint(0, 1000) / 0.2}

r = requests.put("http://localhost:8000/api/products/update/1", json=data)
print(r.content)
