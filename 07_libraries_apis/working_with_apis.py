"""
Working with APIs using the `requests` package.

Install first:
    pip install requests

APIs are how most AI apps get and send data (e.g. calling a weather API,
or the OpenAI/Anthropic API itself).
"""

import requests

# A GET request fetches data from an API
response = requests.get("https://api.github.com/users/octocat")

# Always check the status code before trusting the response
if response.status_code == 200:
    data = response.json()  # parse the JSON response into a Python dict
    print(data["login"], "-", data["public_repos"], "public repos")
else:
    print(f"Request failed with status {response.status_code}")

# Sending query parameters
params = {"q": "python ai", "sort": "stars"}
search_response = requests.get(
    "https://api.github.com/search/repositories", params=params
)
if search_response.status_code == 200:
    results = search_response.json()
    print(f"Found {results.get('total_count', 0)} repositories")
else:
    print(f"Search failed with status {search_response.status_code}")

# POST requests send data to an API (e.g. creating something, or calling
# an AI model with a prompt). This is illustrative — no real key here.
# payload = {"prompt": "Hello, AI!"}
# headers = {"Authorization": "Bearer YOUR_API_KEY"}
# requests.post("https://api.example.com/generate", json=payload, headers=headers)

# Basic error handling around network calls
try:
    r = requests.get("https://api.github.com", timeout=5)
    r.raise_for_status()  # raises an exception for 4xx/5xx responses
except requests.exceptions.RequestException as e:
    print(f"API call failed: {e}")
