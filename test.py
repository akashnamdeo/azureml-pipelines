import requests

url = "http://127.0.0.1:8000/predict"

data = {
    "data": [
        [337, 118, 4, 4.5, 4.5, 9.65, 1],  
        [324, 107, 4, 4, 4.5, 8.87, 1]
    ]
}

headers = {"Content-Type": "application/json"}

response = requests.post(url, json=data, headers=headers)

print(response.json())
