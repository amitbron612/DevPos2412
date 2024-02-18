import requests

#response = requests.delete("http://localhost:8080/items/1")
response = requests.get("http://localhost:8080/items")
print(response.json())
actual = len(response.json())
expected = 2
assert actual == expected