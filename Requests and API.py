# ===========================================================
# Making HTTP requests
# ===========================================================

import requests

# GET request
r = requests.get("https://api.github.com")
print(r.status_code)
print(r.json())

# GET with parameters
params = {"q": "python", "sort": "stars"}
r = requests.get("https://api.github.com/search/repositories", params=params)

# POST request
payload = {"username": "alice", "password": "secret"}
r = requests.post("https://example.com/api/login", json=payload)

# Headers
headers = {"Authorization": "Bearer TOKEN"}
r = requests.get("https://api.example.com/data", headers=headers)

# Handling errors
if r.ok:
    print("Success")
else:
    print("Error:", r.status_code)
