import requests
from core.config import META_ACCESS_TOKEN, META_AD_ACCOUNT_ID

GRAPH_URL = "https://graph.facebook.com/v18.0"

def create_campaign(name, objective="ENGAGEMENT"):
    url = f"{GRAPH_URL}/act_{META_AD_ACCOUNT_ID}/campaigns"
    data = {
        "name": name,
        "objective": objective,
        "status": "PAUSED",
        "special_ad_categories": [],
        "access_token": META_ACCESS_TOKEN
    }
    r = requests.post(url, data=data)
    return r.json()

def create_adset(campaign_id, daily_budget=5000):
    url = f"{GRAPH_URL}/act_{META_AD_ACCOUNT_ID}/adsets"
    data = {
        "name": "AI Adset",
        "campaign_id": campaign_id,
        "daily_budget": daily_budget,
        "billing_event": "IMPRESSIONS",
        "optimization_goal": "POST_ENGAGEMENT",
        "bid_strategy": "LOWEST_COST_WITHOUT_CAP",
        "targeting": {
            "geo_locations": {"countries": ["ZA"]},
            "age_min": 18,
            "age_max": 45
        },
        "status": "PAUSED",
        "access_token": META_ACCESS_TOKEN
    }
    r = requests.post(url, json=data)
    return r.json()

def create_ad_creative(message, page_id):
    url = f"{GRAPH_URL}/act_{META_AD_ACCOUNT_ID}/adcreatives"
    data = {
        "name": "AI Creative",
        "object_story_spec": {
            "page_id": page_id,
            "link_data": {
                "message": message,
                "link": "https://facebook.com"
            }
        },
        "access_token": META_ACCESS_TOKEN
    }
    r = requests.post(url, json=data)
    return r.json()

def create_ad(adset_id, creative_id):
    url = f"{GRAPH_URL}/act_{META_AD_ACCOUNT_ID}/ads"
    data = {
        "name": "AI Ad",
        "adset_id": adset_id,
        "creative": {"creative_id": creative_id},
        "status": "PAUSED",
        "access_token": META_ACCESS_TOKEN
    }
    r = requests.post(url, json=data)
    return r.json()

def activate_campaign(campaign_id):
    url = f"{GRAPH_URL}/{campaign_id}"
    data = {
        "status": "ACTIVE",
        "access_token": META_ACCESS_TOKEN
    }
    r = requests.post(url, data=data)
    return r.json()
