import requests
from core.config import META_PAGE_ID, META_ACCESS_TOKEN

GRAPH_URL = "https://graph.facebook.com/v18.0"

def post_facebook_instagram(content):
    url = f"{GRAPH_URL}/{META_PAGE_ID}/feed"
    data = {
        "message": content,
        "access_token": META_ACCESS_TOKEN
    }
    r = requests.post(url, data=data)
    return r.json().get("id")
