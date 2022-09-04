import requests

endpoint = "http://127.0.0.1:8000/api/products/4/update/"

data = {
    "title": "Updated title",
    "price": 1000
}

get_response = requests.put(endpoint, json = data)

print(get_response.status_code)
print(get_response.json())