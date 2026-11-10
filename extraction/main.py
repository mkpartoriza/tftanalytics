import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve our Riot API key
api_key = os.getenv("RIOT_API_KEY")
print("API Key:", api_key)

# Check that we have an API key
if not api_key:
    raise ValueError("Riot API key not found!")

# Retrieve challengers
url = f"https://na1.api.riotgames.com/tft/league/v1/challenger"

params = {
    "queue": "RANKED_TFT"

}
headers = {
    "X-Riot-Token": api_key
}

# Send the request
response = requests.get(
    url, 
    headers=headers, 
    params=params,
    timeout=20)

# Check for errors
response.raise_for_status()

# Convert JSON response into Python data
data = response.json()

# Display results
print("Status:", response.status_code)
print("League:", data["tier"])
print("Number of challengers:", len(data["entries"]))

# Display the first challenger
print(data["entries"][0])

# Test pulling a match
# test PUUID heD5TMXkZFa4HKjYLv65wxB8DOF7XXVoJWbdTvlZUB9grSAKwHkDjzBfRLXBTgo5h6CWkEbXeG6IDQ

