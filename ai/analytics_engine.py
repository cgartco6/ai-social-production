import requests
from core.config import META_PAGE_ID, META_ACCESS_TOKEN

GRAPH = "https://graph.facebook.com/v18.0"

def fetch_page_insights():
    url = f"{GRAPH}/{META_PAGE_ID}/insights"
    params = {
        "metric": "page_impressions,page_engaged_users,page_fans",
        "access_token": META_ACCESS_TOKEN
    }
    return requests.get(url, params=params).json()
