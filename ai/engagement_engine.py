import requests
from core.config import META_ACCESS_TOKEN

GRAPH = "https://graph.facebook.com/v18.0"

def fetch_comments(post_id):
    url = f"{GRAPH}/{post_id}/comments"
    return requests.get(url, params={"access_token": META_ACCESS_TOKEN}).json()

def reply_to_comment(comment_id, message):
    url = f"{GRAPH}/{comment_id}/replies"
    return requests.post(url, data={
        "message": message,
        "access_token": META_ACCESS_TOKEN
    }).json()
