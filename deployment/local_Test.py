import requests

# The URL would be the public DNS of your EC2 instance once deployed
url = "http://localhost:5000/predict"

data = {
    "features": {
        "attr_a": 1,
        "attr_b": "c",
        "attr_c": 0.55,
        "attr_d": 3
    }
}

response = requests.post(url, json=data)
print(response.json())
