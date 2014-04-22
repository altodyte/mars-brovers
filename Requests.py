import requests

response = requests.get("http://localhost:5000/Jefferson")
print response.content
