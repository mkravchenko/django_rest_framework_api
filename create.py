import requests
import random
import string
from datetime import datetime
import json

data = {
    "title": ''.join(random.choice(string.ascii_letters) for i in range(5)),
    
    "price": random.randint(0, 1000) / 0.1}

r = requests.post("http://localhost:8000/api/products/", json=data)
print(r.content)