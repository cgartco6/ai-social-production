import requests
from core.config import META_PAGE_ID, META_ACCESS_TOKEN
from ai.llm_engine import generate_text

GRAPH_URL = "https://graph.facebook.com/v18.0"

def fetch_comments(post_id):
    url = f"{GRAPH_URL}/{post_id}/comments"
    params = {"access_token": META_ACCESS_TOKEN}
    return requests.get(url, params=params).json()

def auto_reply(comment_id, message):
    url = f"{GRAPH_URL}/{comment_id}/replies"
    data = {
        "message": message,
        "access_token": META_ACCESS_TOKEN
    }
    return requests.post(url, data=data).json()

def handle_engagement(post_id):
    comments = fetch_comments(post_id)
    for c in comments.get("data", []):
        reply = generate_text(f"Reply professionally to: {c['message']}")
        auto_reply(c["id"], reply)
