import requests

GITHUB_TOKEN = "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ0123456789ef"

def get_user():
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    return requests.get("https://api.github.com/user", headers=headers)
