import requests

# r = requests.get("http://localhost:8000/api", json={"query": "Hello"})
# print(r.content)

r = requests.post("http://localhost:8000/api/", json={"title": "Hello"})
print(r.content)
